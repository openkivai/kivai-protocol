import unittest
import requests
from kivai_sdk.intent_parser import parse_input

class TestIntentPipeline(unittest.TestCase):
    def test_turn_on_light(self):
        raw_input = "Turn on the light in the kitchen"
        parsed = parse_input(raw_input)

        response = requests.post("http://127.0.0.1:5000/intent", json=parsed)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "success")
        self.assertIn("Light turned on", data["message"])

if __name__ == '__main__':
    unittest.main()
