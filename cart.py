# cart.py

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def display_cart(self):
        print("Shopping Cart:")
        for item in self.items:
            print(f"{item['product']['name']} - Quantity: {item['quantity']}")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['product']['price'] * item['quantity']
        return total

    def save_cart(self):
        # Save shopping cart state to a file or database
        pass
