class InventoryManager:
    def __init__(self):
        self.stock = {"apple": 10, "banana": 5}
        
    def add_item(self, item_name, quantity):
        self.stock[item_name] = self.stock.get(item_name, 0) + quantity
        
    def remove_item(self, item_name, quantity):
        if self.stock[item_name] - quantity < 0:
            raise ValueError("Not enough stock")
        self.stock[item_name] -= quantity

    def calculate_total_value(self, prices):
        total = 0
        for item, count in self.stock.items():
            # Fixed bug: use .get() to avoid KeyError
            total += count * prices.get(item, 0)
        return total
