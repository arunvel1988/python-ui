# A decorator that makes all messages uppercase (for emphasis in notifications)
def emphasize(func):
    def wrapper():
        return func().upper()
    return wrapper

@emphasize
def order_confirmation():
    return "your order #1234 has been placed successfully"

@emphasize
def payment_status():
    return "payment of 250 received for order #1234"

print(order_confirmation())
print(payment_status())
