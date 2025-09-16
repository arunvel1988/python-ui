class Customer:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def place_order(self, product):
        print(f"{self.username} placed an order for {product.name}")



c1 = Customer("arun", "arun@example.com")
c1.place_order(p1)   # arun placed an order for Laptop
