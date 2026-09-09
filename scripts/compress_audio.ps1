# PowerShell Audio Compression Script for Devotional Chants
# Converts master MP3/WAV tracks to 80 kbps AAC-LC M4A files for offline embedding

$ErrorActionPreference = "Stop"

$ProjectRoot = Resolve-Path "$PSScriptRoot\.."
$InputDir = Join-Path $ProjectRoot "raw_audio"
$OutputDir = Join-Path $ProjectRoot "app\src\main\res\raw"

if (-not (Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
}

# Find FFmpeg binary
$Ffmpeg = Get-Command "ffmpeg" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source -ErrorAction SilentlyContinue
if (-not $Ffmpeg) {
    $ClipGrabFfmpeg = "C:\Program Files (x86)\ClipGrab\ffmpeg.exe"
    if (Test-Path $ClipGrabFfmpeg) {
        $Ffmpeg = $ClipGrabFfmpeg
    }
}

if (-not $Ffmpeg) {
    Write-Error "FFmpeg executable not found! Please install FFmpeg or ensure it is in your PATH."
    exit 1
}

Write-Host "Using FFmpeg: $Ffmpeg" -ForegroundColor Cyan

$Files = Get-ChildItem -Path $InputDir -Include *.mp3, *.wav, *.flac, *.m4a, *.aac -File -Recurse
if ($Files.Count -eq 0) {
    Write-Host "No raw audio files found in $InputDir." -ForegroundColor Yellow
    Write-Host "Place your 6 devotional tracks (MP3/WAV) in $InputDir and re-run this script." -ForegroundColor Yellow
    exit 0
}

foreach ($file in $Files) {
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($file.Name).ToLower() -replace '[ -]', '_'
    $outputFile = Join-Path $OutputDir "$baseName.m4a"

    Write-Host "Compressing: $($file.Name) -> $baseName.m4a ..." -ForegroundColor Green

    & $Ffmpeg -y -i $file.FullName `
        -vn `
        -c:a aac -b:a 80k `
        -ar 44100 `
        -filter:a "highpass=f=60,lowpass=f=16500,loudnorm=I=-16:TP=-1.5:LRA=11" `
        $outputFile

    if ($LASTEXITCODE -eq 0) {
        $sizeKb = [math]::Round((Get-Item $outputFile).Length / 1KB, 1)
        Write-Host "Success: $baseName.m4a ($sizeKb KB)" -ForegroundColor Cyan
    } else {
        Write-Warning "Failed to compress $($file.Name)"
    }
}

$TotalBytes = (Get-ChildItem -Path $OutputDir -Filter *.m4a | Measure-Object -Property Length -Sum).Sum
$TotalMb = [math]::Round($TotalBytes / 1MB, 2)
Write-Host "`nAll audio processed. Total raw audio size in res/raw: $TotalMb MB" -ForegroundColor Magenta
