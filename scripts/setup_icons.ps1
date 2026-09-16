$ProjectRoot = Resolve-Path "$PSScriptRoot\.."
$ffmpeg = $env:FFMPEG_PATH
if (-not $ffmpeg -or -not (Test-Path $ffmpeg)) {
    $ffmpeg = Get-Command "ffmpeg" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source -ErrorAction SilentlyContinue
}
if (-not $ffmpeg -or -not (Test-Path $ffmpeg)) {
    $ClipGrabFfmpeg = "C:\Program Files (x86)\ClipGrab\ffmpeg.exe"
    if (Test-Path $ClipGrabFfmpeg) { $ffmpeg = $ClipGrabFfmpeg }
}
if (-not $ffmpeg) { $ffmpeg = "ffmpeg" }

$src = Join-Path $ProjectRoot "app\src\main\res\drawable\app_icon.png"
$resDir = Join-Path $ProjectRoot "app\src\main\res"


$densities = @{
    "mipmap-mdpi" = 48
    "mipmap-hdpi" = 72
    "mipmap-xhdpi" = 96
    "mipmap-xxhdpi" = 144
    "mipmap-xxxhdpi" = 192
}

foreach ($bucket in $densities.Keys) {
    $dir = Join-Path $resDir $bucket
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    $px = $densities[$bucket]
    $outSquare = Join-Path $dir "ic_launcher.png"
    $outRound = Join-Path $dir "ic_launcher_round.png"
    
    & $ffmpeg -y -i $src -vf "scale=${px}:${px}" $outSquare
    Copy-Item -Path $outSquare -Destination $outRound -Force
    Write-Host "Created $bucket ($px x $px)"
}
Write-Host "All density buckets successfully generated!" -ForegroundColor Green
