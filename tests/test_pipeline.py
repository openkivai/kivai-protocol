import unittest
from unittest.mock import patch
from kivai_sdk.intent_parser import parse_input


class TestIntentPipeline(unittest.TestCase):

    @patch('kivai_sdk.intent_parser.requests.post')
    def test_turn_on_light(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"status": "success"}

        raw_input = "Please turn on the kitchen light"
        command, status = parse_input(raw_input)

        self.assertIn("intent", command)
        self.assertEqual(command["intent"], "TURN_ON_LIGHT")

