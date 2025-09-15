from ecomm_utils import Cart, apply_coupon, order_summary

# Create a cart
cart = Cart()
cart.add_item("Shoes", 2000, qty=1)
cart.add_item("T-Shirt", 500, qty=2)

# Apply discount
total = cart.total()
discounted = apply_coupon(total, 10)  # 10% off

# Print order summary
print(order_summary(cart))
print(f"Discounted Total = {discounted}")
