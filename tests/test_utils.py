import unittest
from src.utils import validate_url

class TestUtils(unittest.TestCase):
    def test_validate_url(self):
        self.assertTrue(validate_url("https://<TARGET>"))
        self.assertFalse(validate_url("invalid-url"))

if __name__ == "__main__":
    unittest.main()
