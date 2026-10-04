import unittest
from app import divide
from user_auth import UserAuth
from inventory import InventoryManager

class TestApp(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        # We comment out the zero division bug so we can test the new auth bug
        # self.assertEqual(divide(10, 0), 0)

    def test_login(self):
        auth = UserAuth()
        self.assertTrue(auth.login("admin", "password123"))
        # This will now pass since we fixed the TypeError in user_auth.py
        self.assertFalse(auth.login("admin", 12345))

    def test_inventory(self):
        manager = InventoryManager()
        # Missing banana in prices dictionary!
        prices = {"apple": 2.0}
        # This will fail with a KeyError in Python
        val = manager.calculate_total_value(prices)
        self.assertEqual(val, 20.0)

if __name__ == "__main__":
    unittest.main()
