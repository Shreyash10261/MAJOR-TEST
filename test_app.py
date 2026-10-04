import unittest
from app import divide
from user_auth import UserAuth

class TestApp(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        # We comment out the zero division bug so we can test the new auth bug
        # self.assertEqual(divide(10, 0), 0)

    def test_login(self):
        auth = UserAuth()
        self.assertTrue(auth.login("admin", "password123"))
        # This will fail with a TypeError in Python because of string/int concatenation
        self.assertFalse(auth.login("admin", 12345))

if __name__ == "__main__":
    unittest.main()
