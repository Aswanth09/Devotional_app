# Raw Audio Staging Directory

Place your original master devotional audio files (MP3, WAV, or FLAC) in this directory.

### Target Track Mapping:
1. `vishnu_sahasranamam.mp3` (or `.wav`) -> Sri Vishnu Sahasranama Stotram (MS Subbulakshmi or standard rendition)
2. `hanuman_chalisa.mp3` (or `.wav`) -> Hanuman Chalisa (Hariharan / MS Subbulakshmi / Gulshan Kumar rendition)
3. `govinda_namalu.mp3` (or `.wav`) -> Govinda Namalu (Tirumala Balaji Chants)
4. `lakshmi_ashtottaram.mp3` (or `.wav`) -> Sri Lakshmi Ashtottara Shatanamavali
5. `garuda_gamana.mp3` (or `.wav`) -> Garuda Gamana Tava Charana
6. `krishna_ashtakam.mp3` (or `.wav`) -> Sri Krishna Ashtakam

### How to Process:
Run the compression script from the project root:
```powershell
.\scripts\compress_audio.ps1
```
or
```cmd
.\scripts\compress_audio.bat
```

This will encode all 6 tracks into speech-optimized 80 kbps AAC-LC M4A files in `app/src/main/res/raw/`, perfectly balancing audio clarity with the < 100 MB budget.
