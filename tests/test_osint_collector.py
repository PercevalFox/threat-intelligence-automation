import unittest
from src.osint_collector import fetch_osint_data

class TestOSINTCollector(unittest.TestCase):
    def test_fetch_osint_data(self):
        url = "https://<TARGET>/osint-feed1"
        data = fetch_osint_data(url)
        self.assertIsInstance(data, list)

if __name__ == "__main__":
    unittest.main()
