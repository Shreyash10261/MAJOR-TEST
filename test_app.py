import unittest
from app import divide
from user_auth import UserAuth
from inventory import InventoryManager
from data_parser import process_data
from currency_converter import convert_to_usd
from payment_gateway import process_batch_payments

class TestApp(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_login(self):
        auth = UserAuth()
        self.assertTrue(auth.login("admin", "password123"))
        self.assertFalse(auth.login("admin", 12345))

    def test_inventory(self):
        manager = InventoryManager()
        prices = {"apple": 2.0}
        val = manager.calculate_total_value(prices)
        self.assertEqual(val, 20.0)

    def test_parser(self):
        valid_data = ["10", "20", "30"]
        self.assertEqual(process_data(valid_data), 60)
        dirty_data = ["10", "20", "N/A", "30"]
        self.assertEqual(process_data(dirty_data), 60)
        
    def test_currency(self):
        # Now this will pass because we added float() casting
        result = convert_to_usd([100.0, 50.0], "1.2")
        self.assertEqual(result, [120.0, 60.0])

    def test_payment(self):
        # Intentional bug: passing a transaction ID without a hyphen raises IndexError
        tx_ids = ["US-12345", "EU-98765", "INVALIDID"]
        regions = process_batch_payments(tx_ids)
        self.assertEqual(regions, ["US", "EU"])

if __name__ == "__main__":
    unittest.main()
