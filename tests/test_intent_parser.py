import unittest
from kivai_sdk.intent_parser import parse_input

class TestIntentParser(unittest.TestCase):
    def test_parse_turn_off_lights(self):
        input_text = "Turn off the lights in the kitchen"
        command = parse_input(input_text)
        self.assertEqual(command["command"], "turn off")
        self.assertEqual(command["object"], "light")
        self.assertEqual(command["location"], "kitchen")

    def test_unknown_command(self):
        input_text = "Do something strange"
        command = parse_input(input_text)
        self.assertEqual(command["command"], "unknown")
        self.assertEqual(command["object"], "unknown")

if __name__ == '__main__':
    unittest.main()
