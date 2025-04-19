# 📝 Whisper Transcription Module

This module uses OpenAI's Whisper to transcribe audio files to text.

## 📂 Files

- `whisper_transcriber.py`: Core logic to load the Whisper model and transcribe audio.
- `run_transcriber.py`: A simple runner script that uses the transcriber.

## ▶️ How to Use

1. Make sure you have installed [ffmpeg](https://ffmpeg.org/download.html) and `openai-whisper`.

2. Update `run_transcriber.py` to point to your audio file:

   ```python
   audio_file = "C:/Users/YourName/PathToYourAudio/sample.mp3"
