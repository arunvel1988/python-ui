def generate_order_ids(start, end):
    for order_id in range(start, end + 1):
        yield f"ORD{order_id:04d}"

orders = generate_order_ids(1, 5)
for o in orders:
    print(o)
