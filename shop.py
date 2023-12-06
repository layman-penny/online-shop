# shop.py

from cart import ShoppingCart
from inventory import ProductInventory

class OnlineShop:
    def __init__(self):
        self.inventory = ProductInventory()
        self.cart = ShoppingCart()

    def load_products(self):
        self.inventory.load_products()

    def display_products(self):
        self.inventory.display_products()

    def add_to_cart(self):
        product_id = input("Enter the ID of the product to add to the cart: ")
        quantity = int(input("Enter the quantity: "))
        self.cart.add_item(self.inventory.get_product_by_id(product_id), quantity)

    def view_cart(self):
        self.cart.display_cart()

    def checkout(self):
        total_amount = self.cart.calculate_total()
        print(f"Total amount to pay: ${total_amount}")
        # Additional checkout logic can be added here
        print("Checkout successful. Thank you for shopping!")

    def save_state(self):
        self.inventory.save_products()
        self.cart.save_cart()
