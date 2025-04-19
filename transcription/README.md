# Transcription Module

This module provides a simple interface to transcribe audio files using OpenAI's Whisper model.

## Files

- `whisper_transcriber.py`: A class that wraps the Whisper transcription model.
- `run_transcriber.py`: A script to run the transcription process from the command line.

## Requirements

Make sure you have the following installed:

- Python 3.10 or newer
- `whisper` (Install via `pip install openai-whisper`)
- `ffmpeg` (Must be installed and accessible in your system PATH)

## How to Use

To transcribe an audio file:

```bash
python run_transcriber.py
