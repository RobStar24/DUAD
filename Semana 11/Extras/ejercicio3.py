class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - Price: {self.price} - Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        if not self.products:
            print("The inventory is empty")
        else:
            for product in self.products:
                print(product)

    def calculate_total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total


product1 = Product("Laptop", 1500, 10)
product2 = Product("Mouse", 10, 50)
product3 = Product("Keyboard", 30, 30)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

total_value = inventory.calculate_total_value()

print("Products in the inventory:")
inventory.show_products()

print(f"\nTotal inventory value: {total_value}")
