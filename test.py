import unittest
from unittest.mock import patch
import logging
from fetch import fectch_by_name
from display import display_git

class TestGitHubEvents(unittest.TestCase):
    @patch("fetch.requests.get")
    def test_fectch_by_name_invalid_user(self, mock_get):
        mock_get.return_value.status_code = 404
        with self.assertLogs(level=logging.ERROR) as log:
            result = fectch_by_name("invalid_user")
            self.assertIsNone(result)
            self.assertIn("Error: Invalid username", log.output[0])

    def test_display_git(self):
        sample_data = '''[
            {
                "type": "CreateEvent",
                "repo": {"name": "test/repo1"}
            },
            {
                "type": "PushEvent",
                "repo": {"name": "test/repo2"}
            }
        ]'''
        with self.assertLogs(level=logging.INFO) as log:
            display_git(sample_data)
            self.assertIn("CreateEvent in test/repo1", log.output[0])
            self.assertIn("PushEvent in test/repo2", log.output[1])

if __name__ == "__main__":
    unittest.main()
