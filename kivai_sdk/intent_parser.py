# kivai_sdk/intent_parser.py
import re
import requests  # New: Used to call the mock device

def send_to_device(command: dict):
    url = "http://127.0.0.1:5000/intent"  # Your Flask mock_light server
    response = requests.post(url, json=command)
    return response.json()

def parse_input(raw_input: str, user_id="abc123", language="en", trigger="Kivai") -> tuple[dict, dict]:
    raw_input = raw_input.lower()

    command = None
    object_ = None
    location = None

    if "turn on" in raw_input:
        command = "turn on"
    elif "turn off" in raw_input:
        command = "turn off"

    if "light" in raw_input or "lights" in raw_input:
        object_ = "light"
    elif "thermostat" in raw_input:
        object_ = "thermostat"

    match = re.search(r"in the (\w+ ?\w*)", raw_input)
    if match:
        location = match.group(1)

    confidence = 0.9 if command and object_ else 0.5

    parsed_command = {
        "command": command or "unknown",
        "object": object_ or "unknown",
        "location": location or "unknown",
        "confidence": confidence,
        "trigger": trigger,
        "language": language,
        "user_id": user_id
    }

    # Send to device
    response = send_to_device(parsed_command)

    return parsed_command, response
