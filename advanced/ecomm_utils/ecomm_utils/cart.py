class Cart:
    def __init__(self):
        self.items = []  # [{name, price, qty}]

    def add_item(self, name, price, qty=1):
        self.items.append({"name": name, "price": price, "qty": qty})

    def remove_item(self, name):
        self.items = [item for item in self.items if item["name"] != name]

    def total(self):
        return sum(item["price"] * item["qty"] for item in self.items)
