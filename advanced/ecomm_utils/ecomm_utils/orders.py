def order_summary(cart):
    """Generate summary of cart"""
    lines = []
    for item in cart.items:
        lines.append(f"{item['name']} x {item['qty']} = {item['price'] * item['qty']}")
    lines.append(f"TOTAL = {cart.total()}")
    return "\n".join(lines)
