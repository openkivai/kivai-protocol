import json
from jsonschema import validate, ValidationError

def validate_command(command: dict) -> tuple[bool, str]:
    """Validates a Kivai command against the official schema."""
    try:
        with open("schema/kivai-command.schema.json", "r") as f:
            schema = json.load(f)
        validate(instance=command, schema=schema)
        return True, "✅ Command is valid!"
    except ValidationError as e:
        return False, f"❌ Validation failed: {e.message}"
    except FileNotFoundError:
        return False, "❌ Schema file not found."
