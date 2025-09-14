orders_list = ["ORD0001", "ORD0002", "ORD0003"]

# Convert list to iterator
orders_iterator = iter(orders_list)

print(next(orders_iterator))  # ORD0001
print(next(orders_iterator))  # ORD0002
print(next(orders_iterator))  # ORD0003

