# inventory.py

import json

class ProductInventory:
    def __init__(self):
        self.products = []

    def load_products(self):
        try:
            with open("products.json", "r") as file:
                self.products = json.load(file)
        except FileNotFoundError:
            pass

    def display_products(self):
        print("Available Products:")
        for product in self.products:
            print(f"{product['id']}. {product['name']} - ${product['price']}")

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product['id'] == product_id:
                return product
        return None

    def save_products(self):
        with open("products.json", "w") as file:
            json.dump(self.products, file)
