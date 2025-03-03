# coffee_menu.py

class CoffeeMenu:
    def __init__(self):
        # Set up initial menu with coffee items and prices
        self.menu = {
            'espresso': 2.50,
            'latte': 2.75,
            'cappuccino': 3.20,
            'americano': 2.70
        }

    # Get the price of an existing coffee item
    def get_price(self, item):
        if item in self.menu:
            return self.menu[item]
        else:
            raise ValueError(f"Item '{item}' not found on the menu")

    # Add a new coffee item to the menu
    def add_item(self, item, price):
        if item in self.menu:
            raise ValueError(f"Item '{item}' already exists on the menu")
        self.menu[item] = price
