# Automated Devotional Audio Downloader using yt-dlp & FFmpeg
$ErrorActionPreference = "Stop"

$ProjectRoot = Resolve-Path "$PSScriptRoot\.."
$RawAudioDir = Join-Path $ProjectRoot "raw_audio"
$YtDlp = Join-Path $PSScriptRoot "yt-dlp.exe"
$Ffmpeg = $env:FFMPEG_PATH
if (-not $Ffmpeg -or -not (Test-Path $Ffmpeg)) {
    $Ffmpeg = Get-Command "ffmpeg" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source -ErrorAction SilentlyContinue
}
if (-not $Ffmpeg -or -not (Test-Path $Ffmpeg)) {
    $ClipGrabFfmpeg = "C:\Program Files (x86)\ClipGrab\ffmpeg.exe"
    if (Test-Path $ClipGrabFfmpeg) { $Ffmpeg = $ClipGrabFfmpeg }
}
if (-not $Ffmpeg) {
    $Ffmpeg = "ffmpeg"
}

if (-not (Test-Path $RawAudioDir)) {
    New-Item -ItemType Directory -Force -Path $RawAudioDir | Out-Null
}

$tracks = @(
    @{
        filename = "vishnu_sahasranamam.mp3"
        query    = "ytsearch1:Vishnu Sahasranamam MS Subbulakshmi Original Full"
        name     = "Sri Vishnu Sahasranama Stotram"
    },
    @{
        filename = "hanuman_chalisa.mp3"
        query    = "ytsearch1:Hanuman Chalisa Hariharan Full Song T-Series"
        name     = "Sri Hanuman Chalisa"
    },
    @{
        filename = "govinda_namalu.mp3"
        query    = "ytsearch1:Govinda Namalu Full Song Telugu Devotional"
        name     = "Govinda Namalu"
    },
    @{
        filename = "lakshmi_ashtottaram.mp3"
        query    = "ytsearch1:Lakshmi Ashtottara Shatanamavali Stotram Full"
        name     = "Sri Lakshmi Ashtottara Shatanamavali"
    },
    @{
        filename = "garuda_gamana.mp3"
        query    = "ytsearch1:Garuda Gamana Tava Charana Full Song"
        name     = "Garuda Gamana Tava Charana"
    },
    @{
        filename = "krishna_ashtakam.mp3"
        query    = "ytsearch1:Krishna Ashtakam Full Song Telugu"
        name     = "Sri Krishna Ashtakam"
    }
)

Write-Output "=========================================================="
Write-Output " Starting Devotional Audio Acquisition for 6 Core Tracks "
Write-Output "=========================================================="

foreach ($t in $tracks) {
    $targetPath = Join-Path $RawAudioDir $t.filename
    Write-Output "`n[DOWNLOAD] $($t.name)..."
    Write-Output " Target: $targetPath"
    Write-Output " Query: $($t.query)"
    
    # Run yt-dlp
    & $YtDlp --ffmpeg-location $Ffmpeg -x --audio-format mp3 --no-playlist -o $targetPath $t.query
    
    if (Test-Path $targetPath) {
        $sizeMB = [math]::Round((Get-Item $targetPath).Length / 1MB, 2)
        Write-Output " [SUCCESS] Downloaded $($t.filename) ($sizeMB MB)"
    } else {
        Write-Warning " [WARNING] Failed to produce $targetPath"
    }
}

Write-Output "`n=========================================================="
Write-Output " Completed Audio Downloads in $RawAudioDir"
Write-Output "=========================================================="
Get-ChildItem -Path $RawAudioDir -Filter "*.mp3" | Select-Object Name, @{Name="Size(MB)";Expression={[math]::Round($_.Length/1MB,2)}}
