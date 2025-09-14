# Decorator to highlight messages (convert to uppercase)
def highlight(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@highlight
def greet_customer(name):
    return "Welcome " + name + ", thanks for shopping with Arun's E-Store!"

@highlight
def order_confirmation(order_id):
    return f"Your order {order_id} has been placed successfully!"

print(greet_customer("Arun"))
print(order_confirmation("ORD12345"))
