class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self):
        return self.price  # No discount by default

class Electronics(Product):
    def apply_discount(self):
        return self.price * 0.9  # 10% discount

class Clothing(Product):
    def apply_discount(self):
        return self.price * 0.8  # 20% discount

# Objects
e = Electronics("Laptop", 60000)
c = Clothing("Jeans", 2000)

print(f"Discounted Laptop Price: {e.apply_discount()}")
print(f"Discounted Jeans Price: {c.apply_discount()}")
