from whisper_transcriber import WhisperTranscriber

def main():
    audio_file = "sample.mp3"  # Replace with the actual file path
    transcriber = WhisperTranscriber(model_size="base")
    text = transcriber.transcribe(audio_file)
    print("\n--- Transcription Output ---\n")
    print(text)

if __name__ == "__main__":
    main()
