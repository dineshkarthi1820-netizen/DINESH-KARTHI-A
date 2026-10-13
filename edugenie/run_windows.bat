@echo off
title EduGenie
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo Could not create the virtual environment. Make sure Python 3.10+ is installed.
        pause
        exit /b 1
    )
)

echo Installing/updating dependencies...
".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\pip.exe" install -r requirements.txt

if not exist ".env" (
    copy ".env.example" ".env" >nul
    echo.
    echo A .env file was created from .env.example.
    echo Edit .env and add your Gemini API key, then run this file again.
    pause
    exit /b 0
)

echo.
echo Starting EduGenie...
start "" http://127.0.0.1:8000
".venv\Scripts\python.exe" -m uvicorn main:app --host 127.0.0.1 --port 8000
pause
