import unittest
from app import divide

class TestApp(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        # This will fail
        self.assertEqual(divide(10, 0), 0)

if __name__ == "__main__":
    unittest.main()
