# Example of a simple decorator that changes text to uppercase
def make_uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@make_uppercase
def greet():
    return "welcome to python world"

print(greet())



