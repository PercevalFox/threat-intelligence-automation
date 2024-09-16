import unittest
from src.alert_manager import send_alert

class TestAlertManager(unittest.TestCase):
    def test_send_alert(self):
        try:
            send_alert("Test Alert", "This is a test alert message.")
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
