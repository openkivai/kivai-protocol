# tests/test_integration.py

import unittest
from kivai_sdk.intent_parser import parse_input
from kivai_sdk.validator import validate_command

class TestIntegration(unittest.TestCase):
    def test_integration_pipeline(self):
        # Sample transcription input (e.g., from a voice command)
        input_text = "Turn on the lights in the kitchen"

        # Parse the input to generate a structured command
        command = parse_input(input_text)

        # Validate the parsed command
        valid, message = validate_command(command)

        # Assertions
        self.assertTrue(valid)
        self.assertIn("valid", message.lower())
        self.assertEqual(command['command'], 'turn on')
        self.assertEqual(command['object'], 'light')
        self.assertEqual(command['location'], 'kitchen')

if __name__ == '__main__':
    unittest.main()
