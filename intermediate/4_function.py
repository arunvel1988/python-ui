
def greet():
    print("Hello! Welcome to Python functions.")

greet()



def greet_person(name):
    print("Hello", name, "!")
    
greet_person("Arun")
greet_person("Meena")



def add(a, b):
    return a + b

result = add(10, 20)
print("Addition result:", result)



def greet_with_default(name="Student"):
    print("Hello", name)

greet_with_default()
greet_with_default("Arun")



def arithmetic_ops(a, b):
    return a + b, a - b, a * b, a / b

sum_val, diff_val, prod_val, div_val = arithmetic_ops(15, 3)
print("Sum:", sum_val)
print("Difference:", diff_val)
print("Product:", prod_val)
print("Division:", div_val)



def print_fruits(*fruits):
    print("Fruits list:", fruits)

print_fruits("Apple", "Banana", "Cherry")
print_fruits("Mango", "Orange")



def print_student(**details):
    for key, value in details.items():
        print(key, ":", value)

print_student(name="Arun", age=25, course="Python")



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))



square = lambda x: x * x
print("Square of 7 is:", square(7))



def outer_function(text):
    def inner_function():
        print("Inner:", text)
    inner_function()

outer_function("Python is awesome")
