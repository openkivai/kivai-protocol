import unittest
from unittest.mock import patch
from kivai_sdk.intent_parser import parse_input


class TestIntegration(unittest.TestCase):

    @patch('kivai_sdk.intent_parser.requests.post')
    def test_integration_pipeline(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"status": "success"}

        input_text = "Can you turn off the lights in the living room?"
        command, status = parse_input(input_text)

        self.assertIsInstance(command, dict)
        self.assertIn("intent", command)
        self.assertEqual(command["intent"], "TURN_OFF_LIGHT")

