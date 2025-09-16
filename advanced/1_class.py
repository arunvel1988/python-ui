# Class
class Product:
    def __init__(self, name, price):
        self.name = name       # Attribute
        self.price = price     # Attribute

    def display_info(self):    # Method
        print(f"{self.name} - ${self.price}")

# Objects
p1 = Product("Laptop", 55000)
p2 = Product("Shoes", 2500)

p1.display_info()
p2.display_info()
