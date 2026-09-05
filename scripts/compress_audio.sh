#!/usr/bin/env bash
# Automated Audio Compression Script for Bhakti Dhwani
# Encodes master tracks to 80 kbps AAC-LC CBR joint stereo / speech profile with highpass/lowpass/loudnorm filters
# Requires ffmpeg installed

INPUT_DIR="./raw_audio"
OUTPUT_DIR="./app/src/main/res/raw"
mkdir -p "$OUTPUT_DIR"

if [ ! -d "$INPUT_DIR" ]; then
  echo "Input directory $INPUT_DIR not found. Creating empty $INPUT_DIR directory..."
  mkdir -p "$INPUT_DIR"
  exit 0
fi

for file in "$INPUT_DIR"/*.{mp3,wav,m4a,flac}; do
  [ -f "$file" ] || continue
  filename=$(basename -- "$file")
  name="${filename%.*}"
  # Standardize name to valid Android resource identifier (lowercase, underscores)
  clean_name=$(echo "$name" | tr '[:upper:]' '[:lower:]' | tr ' -' '__')
  
  echo "Processing: $filename -> ${clean_name}.m4a"
  ffmpeg -y -i "$file" \
    -vn \
    -c:a aac -b:a 80k \
    -ar 44100 \
    -filter:a "highpass=f=60,lowpass=f=16500,loudnorm=I=-16:TP=-1.5:LRA=11" \
    "$OUTPUT_DIR/${clean_name}.m4a"
done

echo "Compression complete. Total size in raw/:"
du -sh "$OUTPUT_DIR"
