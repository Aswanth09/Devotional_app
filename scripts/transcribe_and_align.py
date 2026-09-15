#!/usr/bin/env python3
"""
Acoustic Audio Extraction & Vocal Alignment Engine
Uses faster-whisper with Voice Activity Detection (VAD) and speech energy recognition
to extract exact millisecond timestamps from devotional audio tracks.
"""

import os
import sys
import json
import argparse
import subprocess
import tempfile
from pathlib import Path

try:
    from faster_whisper import WhisperModel
except ImportError:
    print("Error: faster-whisper is not installed. Run 'pip install faster-whisper' first.", file=sys.stderr)
    sys.exit(1)


def find_ffmpeg() -> str:
    """Find a usable ffmpeg executable."""
    import shutil
    ffmpeg_path = shutil.which("ffmpeg")
    if ffmpeg_path:
        return ffmpeg_path

    # Common Windows fallbacks
    common_paths = [
        r"C:\Program Files (x86)\ClipGrab\ffmpeg.exe",
        r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
        r"C:\ffmpeg\bin\ffmpeg.exe",
    ]
    for p in common_paths:
        if os.path.isfile(p):
            return p
    return "ffmpeg"


def extract_audio_slice(input_audio: str, duration_sec: float, ffmpeg_bin: str) -> str:
    """
    Extract the first duration_sec seconds of audio to a temporary 16kHz mono WAV file
    for optimal and fast Whisper processing.
    """
    temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    temp_wav.close()

    cmd = [
        ffmpeg_bin, "-y",
        "-ss", "0",
        "-t", str(duration_sec),
        "-i", input_audio,
        "-vn",
        "-ar", "16000",
        "-ac", "1",
        "-c:a", "pcm_s16le",
        temp_wav.name
    ]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg slice failed: {result.stderr}")
    return temp_wav.name


def format_timestamp(ms: int) -> str:
    """Convert millisecond timestamp to mm:ss.fff format."""
    total_seconds = ms / 1000.0
    minutes = int(total_seconds // 60)
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:06.3f}"


def transcribe_and_align(
    audio_path: str,
    duration: float = None,
    model_size: str = "base",
    device: str = "cpu",
    compute_type: str = "int8",
    language: str = None,
    output_json: str = None
):
    """
    Process vocal track using faster-whisper with Voice Activity Detection (VAD)
    and extract real speech-energy millisecond timestamps.
    """
    if not os.path.isfile(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    ffmpeg_bin = find_ffmpeg()
    temp_file = None

    if duration is not None and duration > 0:
        print(f"[Engine] Pre-slicing first {duration} seconds using FFmpeg ({ffmpeg_bin})...")
        processed_audio = extract_audio_slice(audio_path, duration, ffmpeg_bin)
        temp_file = processed_audio
    else:
        processed_audio = audio_path

    try:
        print(f"[Engine] Loading WhisperModel(size='{model_size}', device='{device}', compute_type='{compute_type}')...")
        model = WhisperModel(model_size, device=device, compute_type=compute_type)

        print(f"[Engine] Transcribing & aligning acoustics with VAD filtering...")
        segments, info = model.transcribe(
            processed_audio,
            language=language,
            task="transcribe",
            beam_size=5,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=400),
            word_timestamps=True
        )

        detected_lang = info.language
        lang_prob = round(info.language_probability, 3)
        print(f"[Engine] Detected language: '{detected_lang}' (confidence: {lang_prob})")
        print("-" * 75)
        print(f"{'#':<3} | {'TIMESTAMPS':<23} | {'RANGE (ms)':<17} | {'RECOGNIZED VOCALS'}")
        print("-" * 75)

        results = []
        idx = 1
        for segment in segments:
            start_ms = int(round(segment.start * 1000))
            end_ms = int(round(segment.end * 1000))
            text = segment.text.strip()

            words_data = []
            if segment.words:
                for w in segment.words:
                    words_data.append({
                        "word": w.word.strip(),
                        "start_ms": int(round(w.start * 1000)),
                        "end_ms": int(round(w.end * 1000)),
                        "probability": round(float(w.probability), 3)
                    })

            seg_info = {
                "index": idx,
                "start_ms": start_ms,
                "end_ms": end_ms,
                "formatted_start": format_timestamp(start_ms),
                "formatted_end": format_timestamp(end_ms),
                "duration_ms": end_ms - start_ms,
                "text": text,
                "words": words_data
            }
            results.append(seg_info)

            time_str = f"{format_timestamp(start_ms)} -> {format_timestamp(end_ms)}"
            range_ms_str = f"{start_ms} - {end_ms} ms"
            print(f"{idx:<3} | {time_str:<23} | {range_ms_str:<17} | {text}")
            idx += 1

        print("-" * 75)
        print(f"[Engine] Acoustic extraction completed: {len(results)} segments recognized.")

        if output_json:
            out_path = Path(output_json)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump({
                    "audio_file": os.path.basename(audio_path),
                    "detected_language": detected_lang,
                    "language_probability": lang_prob,
                    "total_segments": len(results),
                    "segments": results
                }, f, indent=2, ensure_ascii=False)
            print(f"[Engine] Saved detailed timestamps to: {output_json}")

        return results

    finally:
        if temp_file and os.path.exists(temp_file):
            try:
                os.remove(temp_file)
            except Exception:
                pass


def main():
    parser = argparse.ArgumentParser(description="Extract speech energy and millisecond timestamps from devotional audio.")
    parser.add_argument("audio", help="Path to input audio file (.m4a, .mp3, etc.)")
    parser.add_argument("--duration", type=float, default=None, help="Process only first N seconds (e.g., 60)")
    parser.add_argument("--model", default="base", help="Whisper model size (tiny, base, small, medium, default: base)")
    parser.add_argument("--device", default="cpu", help="Device to run on (cpu, cuda)")
    parser.add_argument("--language", default=None, help="Language code (hi, sa, te, etc.)")
    parser.add_argument("--output", default=None, help="Output JSON path for extracted alignment")

    args = parser.parse_args()
    transcribe_and_align(
        audio_path=args.audio,
        duration=args.duration,
        model_size=args.model,
        device=args.device,
        language=args.language,
        output_json=args.output
    )


if __name__ == "__main__":
    main()
