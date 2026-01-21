#!/usr/bin/env python3
"""
Script runner untuk Chat App - Alternative untuk Makefile
Penggunaan: python run.py [command]
"""

import sys
import os
import subprocess
import time
import threading

def install():
    """Install dependencies"""
    print("📦 Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("✅ Dependencies installed!")

def dev():
    """Run development server"""
    print("🚀 Starting development server...")
    print("🌐 Server will be available at http://localhost:5000")
    print("Press Ctrl+C to stop")
    subprocess.run([sys.executable, "main.py"])

def ngrok():
    """Run with ngrok tunnel"""
    print("🌍 Starting server with ngrok tunnel...")
    print("Make sure ngrok is installed and authenticated!")
    
    # Start Flask server in background
    print("🚀 Starting Flask server...")
    flask_process = subprocess.Popen([sys.executable, "main.py"])
    
    # Wait a bit for server to start
    time.sleep(3)
    
    try:
        print("🔗 Starting ngrok tunnel...")
        ngrok_process = subprocess.run(["ngrok", "http", "5000"])
    except KeyboardInterrupt:
        print("\n🛑 Stopping servers...")
    except FileNotFoundError:
        print("❌ ngrok not found! Please install ngrok first:")
        print("   1. Download from https://ngrok.com/download")
        print("   2. Extract and add to PATH")
        print("   3. Run: ngrok authtoken YOUR_TOKEN")
    finally:
        flask_process.terminate()

def clean():
    """Clean cache files"""
    print("🧹 Cleaning cache files...")
    
    # Remove __pycache__ directories
    for root, dirs, files in os.walk('.'):
        for dir_name in dirs:
            if dir_name == '__pycache__':
                cache_path = os.path.join(root, dir_name)
                try:
                    import shutil
                    shutil.rmtree(cache_path)
                    print(f"   Removed: {cache_path}")
                except Exception as e:
                    print(f"   Error removing {cache_path}: {e}")
    
    # Remove .pyc files
    for root, dirs, files in os.walk('.'):
        for file_name in files:
            if file_name.endswith('.pyc'):
                pyc_path = os.path.join(root, file_name)
                try:
                    os.remove(pyc_path)
                    print(f"   Removed: {pyc_path}")
                except Exception as e:
                    print(f"   Error removing {pyc_path}: {e}")
    
    print("✅ Cache cleaned!")

def test():
    """Run tests"""
    print("🧪 Running tests...")
    print("⚠️  No tests configured yet")

def help_menu():
    """Show help menu"""
    print("🔧 Chat App Runner")
    print("Available commands:")
    print("  python run.py install  - Install dependencies")
    print("  python run.py dev      - Run development server")
    print("  python run.py ngrok    - Run with ngrok tunnel")
    print("  python run.py clean    - Clean cache files")
    print("  python run.py test     - Run tests")
    print("  python run.py help     - Show this help")

def main():
    if len(sys.argv) < 2:
        help_menu()
        return
    
    command = sys.argv[1].lower()
    
    commands = {
        'install': install,
        'dev': dev,
        'ngrok': ngrok,
        'clean': clean,
        'test': test,
        'help': help_menu
    }
    
    if command in commands:
        commands[command]()
    else:
        print(f"❌ Unknown command: {command}")
        help_menu()

if __name__ == "__main__":
    main()