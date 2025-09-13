# ============================================================
# 1. BASIC FUNCTIONS
# ============================================================

# Function without parameters
def say_hello():
    print("Hello, welcome to Python Functions!")

say_hello()


# Function with parameters
def greet_user(name):
    print("Hello", name)

greet_user("Arun")
greet_user("Meena")


# Function with return value
def add_numbers(a, b):
    return a + b

print("Addition:", add_numbers(10, 20))


# ============================================================
# 2. DEFAULT PARAMETERS
# ============================================================

def greet_with_default(name="Student"):
    print("Hello", name)

greet_with_default()
greet_with_default("Arun")


# ============================================================
# 3. MULTIPLE RETURN VALUES
# ============================================================

def operations(a, b):
    return a + b, a - b, a * b, a / b

sum_val, diff_val, prod_val, div_val = operations(12, 3)
print("Sum:", sum_val)
print("Difference:", diff_val)
print("Product:", prod_val)
print("Division:", div_val)


# ============================================================
# 4. VARIABLE ARGUMENTS
# ============================================================

# *args → allows multiple values
def print_fruits(*fruits):
    print("Fruits list:", fruits)

print_fruits("Apple", "Banana", "Cherry")

# **kwargs → allows keyword arguments
def student_info(**info):
    for key, value in info.items():
        print(key, ":", value)

student_info(name="Arun", age=25, course="Python")


# ============================================================
# 5. RECURSION
# ============================================================

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5:", factorial(5))


# ============================================================
# 6. LAMBDA FUNCTIONS (anonymous functions)
# ============================================================

square = lambda x: x * x
print("Square of 6:", square(6))

add = lambda a, b: a + b
print("Lambda Addition:", add(10, 15))


# ============================================================
# 7. FUNCTIONS INSIDE FUNCTIONS (Nested Functions)
# ============================================================

def outer_function(name):
    def inner_function():
        print("Hello from inner function,", name)
    inner_function()

outer_function("Arun")


# ============================================================
# 8. GLOBAL vs LOCAL VARIABLES
# ============================================================

x = "global variable"

def test_variables():
    x = "local variable"
    print("Inside function:", x)

test_variables()
print("Outside function:", x)


# Modify global variable using 'global' keyword
count = 0

def increment():
    global count
    count += 1
    print("Count inside function:", count)

increment()
increment()
print("Count outside:", count)


# ============================================================
# 9. FUNCTION DOCUMENTATION (DOCSTRINGS)
# ============================================================

def multiply(a, b):
    """This function multiplies two numbers and returns the result."""
    return a * b

print("Multiply 4 and 5:", multiply(4, 5))
print("Docstring:", multiply.__doc__)


# ============================================================
# 10. REAL-WORLD E-COMMERCE EXAMPLES
# ============================================================

# Function to calculate discount
def calculate_discount(price, discount_percent=10):
    return price - (price * discount_percent / 100)

print("Price after discount:", calculate_discount(1000, 20))


# Function to calculate total cart value
def cart_total(prices):
    return sum(prices)

print("Cart total:", cart_total([200, 150, 50]))


# Function to apply coupon
def apply_coupon(total, coupon="NONE"):
    if coupon == "WELCOME10":
        return total * 0.9
    elif coupon == "FREESHIP":
        return total  # free shipping, no discount
    else:
        return total

print("Total after coupon:", apply_coupon(500, "WELCOME10"))


# Function with nested business logic
def checkout(cart, coupon=None):
    subtotal = sum(cart)
    print("Subtotal:", subtotal)

    if coupon:
        subtotal = apply_coupon(subtotal, coupon)
        print("Applied coupon:", coupon)

    print("Final total:", subtotal)
    return subtotal

checkout([200, 300, 100], "WELCOME10")
print("Finished processing orders")