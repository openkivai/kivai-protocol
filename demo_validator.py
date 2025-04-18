from kivai_validator import validate_command

sample_command = {
    "command": "turn on",
    "object": "light",
    "location": "kitchen",
    "confidence": 0.95,
    "trigger": "Kivai",
    "language": "en",
    "user_id": "abc123"
}

valid, message = validate_command(sample_command)
print(message)
