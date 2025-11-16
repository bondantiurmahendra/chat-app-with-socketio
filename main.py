# Imports

import os
import random
import logging
from datetime import datetime
from typing import Dict, List, Optional

from flask import Flask, request, render_template, session
from flask_socketio import SocketIO, emit, join_room, leave_room
from werkzeug.middleware.proxy_fix import ProxyFix

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() in ('True', '1', 't')
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*')

    # Chat rooms
    CHAT_ROOMS = [
        'General',
        'Zero to Knowing',
        'The Bookshelf',
        'The Nerd Nook',
    ]
        


app = Flask(__name__)
app.config.from_object(Config)

# Handle Reverse Proxy
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

#Setup SocketIO
socketIO = SocketIO(
    app, 
    cors_allowed_origins=app.config['CORS_ORIGINS'],
    logger=True,
    engineio_logger=True
)

# Make a database / Dict
active_users : Dict[str, dict] = {}

# Make a User
def generate_guest_username() -> str:
    timestamp = datetime.now().strftime('%H%M')
    return f'Guest-{timestamp}{random.randint(1000, 9999)}'

# Home Route
@app.route('/')
def index():
    if 'username' not in session:
        session['username'] = generate_guest_username()
        logger.info(f'New user: {session["username"]}')
    return render_template(
        'index.html', 
        username=session['username'], 
        rooms=app.config['CHAT_ROOMS']
    )


# Make a connection
@socketIO.event
def connect():
    try:
        if 'username' not in session:
            session['username'] = generate_guest_username()
            
        active_users[request.sid] = {
            'username': session['username'],
            'connected_at': datetime.now().isoformat()
        }

        emit('active_users', {
            'users': [user['username'] for user in active_users.values()]
        }, broadcast=True)
        
        logger.info(f'User connected: {session["username"]}')

    except Exception as e:
        logger.error(f'Failed to connect: {e}')
        return False


# Make a disconnection
@socketIO.event
def disconnect():
    try:
        if request.sid in active_users:
            username = active_users[request.sid]['username']
            del active_users[request.sid]

            emit('active_users', {
                'users': [user['username'] for user in active_users.values()]
            }, broadcast=True)
            
            logger.info(f'User disconnected: {username}')

    except Exception as e:
        logger.error(f'Failed to disconnect: {e}')


@socketIO.on('join')
def on_join(data:dict):
    try:
        username = data['username']
        room = data['room']

        if room not in app.config['CHAT_ROOMS']:
            logger.warning(f'Invalid room: {room}')
            return
        join_room(room)
        active_users[request.sid]['room'] = room

        emit('status', {
            'msg': f'{username} has joined the room!',
            'type': 'join',
            'timestamp': datetime.now().isoformat(),
        }, room=room)

        logger.info(f'User {username} has joined')

    except Exception as e:
        logger.error({e})

@socketIO.on('leave')
def on_leave(data:dict):
    try:
        username = data['username']
        room = data['room']

        leave_room(room)
        if request.sid in active_users:
            active_users[request.sid].pop('room', None)

        emit('status', {
            'msg': f'{username} has left the room!',
            'type': 'leave',
            'timestamp': datetime.now().isoformat(),
        }, room=room)

        logger.info(f'User {username} has left')
    
    except Exception as e:
        logger.error({e})


@socketIO.event
def handle_message(data:dict):
    try:
        username = session['username']
        room = data.get('room', 'General')
        msg_type = data.get('type', 'message')
        message = data.get('msg', '').strip()


        if not message:
            return
        
        timestamp = datetime.now().isoformat()

        if msg_type == 'private':
            target_user = data.get('target_user')
            if not target_user:
                return

            for sid, user_data in active_users.items():
                if user_data['username'] == target_user:
                    emit('private_message', {
                        'from': username,
                        'to': target_user,
                        'msg': message,
                        'timestamp': timestamp,
                    }, room=sid)
                    return

        else:
            if room not in app.config['CHAT_ROOMS']:
                return
            
            emit('message', {
                'username': username,
                'room': room,
                'msg': message,
                'timestamp': timestamp,
            }, room=room)

    except Exception as e:
        logger.error({e})





if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketIO.run(
        app, 
        host='0.0.0.0', 
        port=port,
        debug=app.config['DEBUG'],
        use_reloader=app.config['DEBUG']
    )