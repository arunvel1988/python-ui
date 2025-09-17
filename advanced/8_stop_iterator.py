class OrderIDGenerator:
    def __iter__(self):
        self.order_id = 1001  # start from order #1001
        self.max_orders = 5   # limit to 5 orders
        return self

    def __next__(self):
        if self.order_id < 1001 + self.max_orders:
            current_order = self.order_id
            self.order_id += 1
            return f"Order-{current_order}"
        else:
            raise StopIteration   # stop after 5 orders

order_gen = OrderIDGenerator()
orders = iter(order_gen)

for order in orders:
    print(order)
