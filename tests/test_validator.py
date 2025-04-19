import unittest
import os
import sys

# Dynamically add the kivai-protocol root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from kivai_sdk.kivai_validator import validate_command

SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "..", "kivai_sdk", "schema", "kivai-command.schema.json")

class TestValidator(unittest.TestCase):
    def test_valid_command(self):
        command = {
            "command": "turn on",
            "object": "light",
            "location": "kitchen",
            "confidence": 0.95,
            "trigger": "Kivai",
            "language": "en",
            "user_id": "abc123"
        }

        valid, message = validate_command(command, schema_path=SCHEMA_PATH)
        self.assertTrue(valid)
        self.assertIn("valid", message.lower())

    def test_invalid_command(self):
        command = {
            "command": "turn on",  # ← fixed comma!
            # Missing required fields
        }

        valid, message = validate_command(command, schema_path=SCHEMA_PATH)
        self.assertFalse(valid)
        self.assertIn("required", message.lower())

if __name__ == '__main__':
    unittest.main()


