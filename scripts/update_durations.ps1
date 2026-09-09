# Script to automatically read track durations from app/src/main/res/raw/
# and update durationMs in LocalAudioRepository.kt

$ProjectRoot = Resolve-Path "$PSScriptRoot\.."
$RawDir = Join-Path $ProjectRoot "app\src\main\res\raw"
$RepoFile = Join-Path $ProjectRoot "app\src\main\java\com\bhaktidhwani\app\data\repository\LocalAudioRepository.kt"

# Find FFmpeg binary
$Ffmpeg = Get-Command "ffmpeg" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source -ErrorAction SilentlyContinue
if (-not $Ffmpeg) {
    $ClipGrabFfmpeg = "C:\Program Files (x86)\ClipGrab\ffmpeg.exe"
    if (Test-Path $ClipGrabFfmpeg) { $Ffmpeg = $ClipGrabFfmpeg }
}

if (-not $Ffmpeg) {
    Write-Error "FFmpeg not found! Cannot read audio durations."
    exit 1
}

$Tracks = @(
    "vishnu_sahasranamam",
    "hanuman_chalisa",
    "govinda_namalu",
    "lakshmi_ashtottaram",
    "garuda_gamana",
    "krishna_ashtakam"
)

$RepoContent = Get-Content $RepoFile -Raw

foreach ($track in $Tracks) {
    $filePath = Join-Path $RawDir "$track.m4a"
    if (Test-Path $filePath) {
        $output = & $Ffmpeg -i $filePath 2>&1 | Out-String
        if ($output -match "Duration:\s*(\d+):(\d+):(\d+\.?\d*)") {
            $hours = [int]$matches[1]
            $minutes = [int]$matches[2]
            $seconds = [double]$matches[3]
            $durationMs = [long](($hours * 3600 + $minutes * 60 + $seconds) * 1000)
            
            Write-Host "$track : $durationMs ms ($hours h $minutes m $seconds s)" -ForegroundColor Cyan

            # Regex replace in LocalAudioRepository.kt
            $pattern = "(?s)(id\s*=\s*""$track"".*?durationMs\s*=\s*)\d+L"
            $RepoContent = $RepoContent -replace $pattern, "`${1}${durationMs}L"
        }
    }
}

Set-Content -Path $RepoFile -Value $RepoContent -Encoding UTF8
Write-Host "`nUpdated LocalAudioRepository.kt with exact track durations." -ForegroundColor Green
