class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"{self.name} - ${self.price}")

# Child classes
class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

e1 = Electronics("iPhone", 70000, "1 year")
c1 = Clothing("T-shirt", 500, "L")

e1.display_info()   # iPhone - $70000
c1.display_info()   # T-shirt - $500
