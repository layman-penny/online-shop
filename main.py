# main.py

from shop import OnlineShop

def main():
    online_shop = OnlineShop()
    online_shop.load_products()
    
    while True:
        print("1. Display available products")
        print("2. Add a product to the cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Save and exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            online_shop.display_products()
        elif choice == "2":
            online_shop.add_to_cart()
        elif choice == "3":
            online_shop.view_cart()
        elif choice == "4":
            online_shop.checkout()
        elif choice == "5":
            online_shop.save_state()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
