# Makefile untuk Chat App
.PHONY: help install dev ngrok clean test

# Default target
help:
	@echo "Available commands:"
	@echo "  make install  - Install dependencies"
	@echo "  make dev      - Run development server"
	@echo "  make ngrok    - Run with ngrok tunnel"
	@echo "  make clean    - Clean cache files"
	@echo "  make test     - Run tests (if available)"

# Install dependencies
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Run development server
dev:
	@echo "Starting development server..."
	@echo "Server will be available at http://localhost:5000"
	python main.py

# Run with ngrok
ngrok:
	@echo "Starting server with ngrok tunnel..."
	@echo "Make sure ngrok is installed and authenticated"
	@echo "Starting Flask server in background..."
	@start /B python main.py
	@timeout /t 3 /nobreak > nul
	@echo "Starting ngrok tunnel..."
	ngrok http 5000

# Clean cache files
clean:
	@echo "Cleaning cache files..."
	@if exist __pycache__ rmdir /s /q __pycache__
	@for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
	@if exist *.pyc del /q *.pyc
	@echo "Cache cleaned!"

# Run tests (placeholder)
test:
	@echo "Running tests..."
	@echo "No tests configured yet"