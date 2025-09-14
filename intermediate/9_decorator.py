# Decorator to emphasize greetings by making them uppercase
def emphasize(func):
    def wrapper(customer_name):
        return func(customer_name).upper()
    return wrapper

@emphasize
def greet_customer(name):
    return "Welcome to Arun's E-Shop, " + name

print(greet_customer("Arun"))
print(greet_customer("Priya"))
