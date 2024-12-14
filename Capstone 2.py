class Product:
    def __init__(self, product_id, name, product_description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.product_description = product_description
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity += quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Description: {self.product_description}, Price: {self.price}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self):
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        product_description = input("Enter product description: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter initial quantity: "))
        
        new_product = Product(product_id, name, product_description, price, quantity)
        self.products.append(new_product)
        print(f"Product {name} added successfully.")

    def update_stock(self):
        product_id = input("Enter product ID to update: ")
        found = False
        for product in self.products:
            if product.product_id == product_id:
                quantity = int(input(f"Enter quantity to update (current quantity: {product.quantity}): "))
                product.update_quantity(quantity)
                found = True
                print(f"Updated stock for {product.name}. New quantity: {product.quantity}")
                break
        if not found:
            print(f"Product with ID {product_id} not found.")

    def display_products(self):
        if not self.products:
            print("No products in inventory.")
        else:
            print("\n--- Inventory List ---")
            for product in self.products:
                print(product)

    def calculate_total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Total value of inventory: ${total_value:.2f}")


def main():
    inventory = Inventory()

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add a new product")
        print("2. Update stock quantity")
        print("3. Display all products")
        print("4. Calculate total inventory value")
        print("5. Exit")
        
        choice = input("Select an action (1-5): ")

        if choice == '1':
            inventory.add_product()
        elif choice == '2':
            inventory.update_stock()
        elif choice == '3':
            inventory.display_products()
        elif choice == '4':
            inventory.calculate_total_inventory_value()
        elif choice == '5':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice, please select again.")

if __name__ == "__main__":
    main()
