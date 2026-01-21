# 💬 Aplikasi Chat Real-time

Aplikasi chat berbasis web yang memungkinkan pengguna untuk berkomunikasi secara real-time dalam berbagai ruang obrolan. Dibangun menggunakan Flask dan Socket.IO dengan antarmuka yang modern dan responsif.

## ✨ Fitur Utama

- **Chat Real-time**: Komunikasi instan menggunakan WebSocket
- **Multi-room**: 4 ruang obrolan berbeda (General, Zero to Knowing, The Bookshelf, The Nerd Nook)
- **Pesan Pribadi**: Kirim pesan langsung ke pengguna tertentu dengan format `@username pesan`
- **Daftar Pengguna Online**: Lihat siapa saja yang sedang aktif
- **Username Otomatis**: Sistem otomatis memberikan nama pengguna untuk tamu
- **Antarmuka Modern**: Desain gelap yang nyaman untuk mata
- **Responsive**: Tampilan yang optimal di desktop dan mobile

## 🛠️ Teknologi yang Digunakan

- **Backend**: Python Flask + Flask-SocketIO
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Real-time**: Socket.IO
- **Styling**: CSS Custom dengan tema gelap

## 📋 Persyaratan Sistem

- Python 3.7 atau lebih baru
- pip (Python package manager)
- Browser modern yang mendukung WebSocket

## 🚀 Instalasi dan Penggunaan

### 1. Clone atau Download Project

```bash
# Jika menggunakan git
git clone <repository-url>
cd chat-app

# Atau extract file zip ke folder chat-app
```

### 2. Buat Virtual Environment (Opsional tapi Disarankan)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Environment

```bash
# Salin file konfigurasi
copy .env.example .env

# Edit file .env sesuai kebutuhan (opsional)
```

### 5. Jalankan Aplikasi

#### Opsi 1: Jalankan Manual

```bash
python main.py
```

#### Opsi 2: Menggunakan Script Runner (Rekomendasi)

```bash
# Install dependencies
python run.py install

# Jalankan development server
python run.py dev

# Jalankan dengan ngrok tunnel (untuk akses dari internet)
python run.py ngrok
```

#### Opsi 3: Menggunakan Makefile (jika tersedia)

```bash
# Install dependencies
make install

# Jalankan development server
make dev

# Jalankan dengan ngrok tunnel
make ngrok
```

Aplikasi akan berjalan di `http://localhost:5000`

## 🌐 Menggunakan Ngrok untuk Akses Internet

Ngrok memungkinkan aplikasi lokal Anda diakses dari internet. Berguna untuk:

- Testing di perangkat mobile
- Sharing dengan teman/kolega
- Webhook development

### Setup Ngrok:

1. **Download dan Install Ngrok**
   - Kunjungi https://ngrok.com/download
   - Download sesuai OS Anda
   - Extract dan tambahkan ke PATH

2. **Daftar dan Dapatkan Auth Token**
   - Daftar di https://ngrok.com
   - Copy auth token dari dashboard
   - Jalankan: `ngrok authtoken YOUR_TOKEN`

3. **Jalankan dengan Ngrok**
   ```bash
   python run.py ngrok
   ```
4. **Akses URL Public**
   - Ngrok akan memberikan URL seperti: `https://abc123.ngrok.io`
   - Share URL ini untuk akses dari mana saja

```

Aplikasi akan berjalan di `http://localhost:5000`

## ⚙️ Konfigurasi Environment

Buat file `.env` berdasarkan `.env.example` dan sesuaikan nilai berikut:

| Variable       | Deskripsi                         | Default        |
| -------------- | --------------------------------- | -------------- |
| `SECRET_KEY`   | Kunci rahasia untuk session Flask | Auto-generated |
| `FLASK_DEBUG`  | Mode debug (True/False)           | False          |
| `PORT`         | Port aplikasi                     | 5000           |
| `CORS_ORIGINS` | Domain yang diizinkan untuk CORS  | \*             |

## 🎯 Cara Menggunakan

### Bergabung ke Ruang Chat

1. Buka aplikasi di browser
2. Pilih ruang chat dari sidebar kiri
3. Mulai mengirim pesan

### Mengirim Pesan Pribadi

Gunakan format: `@username pesan anda`
Contoh: `@Guest1234 Halo, apa kabar?`

### Ruang Chat yang Tersedia

- **General**: Obrolan umum untuk semua topik
- **Zero to Knowing**: Diskusi pembelajaran dan edukasi
- **The Bookshelf**: Berbagi tentang buku dan literatur
- **The Nerd Nook**: Diskusi teknologi dan programming

## 📁 Struktur Project

```

chat-app/
├── main.py # File utama aplikasi Flask
├── run.py # Script runner (seperti npm scripts)
├── Makefile # Alternative runner untuk make commands
├── requirements.txt # Dependencies Python
├── .env.example # Template konfigurasi
├── .gitignore # File yang diabaikan Git
├── README.md # Dokumentasi ini
├── static/
│ ├── chat.js # Logic JavaScript untuk chat
│ └── styles.css # Styling CSS
└── templates/
└── index.html # Template HTML utama

````

## 🔧 Script Runner Commands

Proyek ini menyediakan script runner seperti `npm scripts` di Node.js:

```bash
# Menggunakan run.py (cross-platform)
python run.py install    # Install dependencies
python run.py dev        # Run development server
python run.py ngrok      # Run with ngrok tunnel
python run.py clean      # Clean cache files
python run.py test       # Run tests
python run.py help       # Show help

# Menggunakan Makefile (Windows/Linux/Mac)
make install            # Install dependencies
make dev               # Run development server
make ngrok             # Run with ngrok tunnel
make clean             # Clean cache files
make test              # Run tests
````

## 🔧 Development

### Menjalankan dalam Mode Development

```bash
# Set environment variable untuk debug
set FLASK_DEBUG=True
python main.py
```

### Struktur Kode Utama

- **main.py**: Berisi logic server Flask dan Socket.IO handlers
- **chat.js**: Menangani interaksi client-side dan komunikasi WebSocket
- **styles.css**: Styling dengan tema gelap dan animasi
- **index.html**: Template HTML dengan Jinja2

## 🚀 Deployment

### Untuk Production

1. Set `FLASK_DEBUG=False` di file `.env`
2. Gunakan web server seperti Gunicorn:

```bash
pip install gunicorn
gunicorn --worker-class eventlet -w 1 main:app
```

### Menggunakan Docker (Opsional)

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "main.py"]
```

## 🐛 Troubleshooting

### Port Sudah Digunakan

Jika port 5000 sudah digunakan, ubah di file `.env`:

```
PORT=8080
```

### Error Import Module

Pastikan semua dependencies terinstall:

```bash
pip install -r requirements.txt
```

### WebSocket Connection Failed

- Pastikan firewall tidak memblokir port
- Cek apakah browser mendukung WebSocket
- Untuk deployment, pastikan server mendukung WebSocket

## 📝 Catatan Pengembangan

- Aplikasi menggunakan in-memory storage untuk data pengguna (tidak persisten)
- Untuk production, pertimbangkan menggunakan Redis atau database
- Session management menggunakan Flask session dengan cookie
- Logging sudah dikonfigurasi untuk monitoring

## 🤝 Kontribusi

Silakan buat pull request atau laporkan bug melalui issues. Pastikan untuk:

1. Test fitur baru sebelum submit
2. Ikuti style guide yang ada
3. Update dokumentasi jika diperlukan

## 📄 Lisensi

Project ini bebas digunakan untuk keperluan pembelajaran dan pengembangan.

---

**Selamat menggunakan aplikasi chat! 🎉**
