class OrderIDGenerator:
    def __iter__(self):
        self.order_id = 1001  # start from order #1001
        return self

    def __next__(self):
        current_order = self.order_id
        self.order_id += 1
        return f"Order-{current_order}"

order_gen = OrderIDGenerator()
orders = iter(order_gen)

print(next(orders))  # Order-1001
print(next(orders))  # Order-1002
print(next(orders))  # Order-1003
