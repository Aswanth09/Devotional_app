@echo off
setlocal enabledelayedexpansion

echo ========================================================
echo   Bhakti Dhwani - Devotional Audio Batch Compressor
echo ========================================================

set "SCRIPT_DIR=%~dp0"
set "PROJECT_ROOT=%SCRIPT_DIR%.."
set "INPUT_DIR=%PROJECT_ROOT%\raw_audio"
set "OUTPUT_DIR=%PROJECT_ROOT%\app\src\main\res\raw"

if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

set "FFMPEG=ffmpeg"
where ffmpeg >nul 2>nul
if %errorlevel% neq 0 (
    if exist "C:\Program Files (x86)\ClipGrab\ffmpeg.exe" (
        set "FFMPEG=C:\Program Files (x86)\ClipGrab\ffmpeg.exe"
    ) else (
        echo [ERROR] FFmpeg not found in PATH or ClipGrab directory!
        echo Please install FFmpeg to convert your master audio files.
        pause
        exit /b 1
    )
)

echo Using FFmpeg: "%FFMPEG%"
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_DIR%compress_audio.ps1"

pause
