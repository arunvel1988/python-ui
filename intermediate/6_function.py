# Function with *args (variable number of arguments)

def show_topper(*students):
    print("The best performer is", students[0])

show_topper("Ananya", "Rahul", "Kiran", "Meera")


def favourite_book(*books):
    print("My all-time favourite is", books[-1])   # last one

favourite_book("Python Basics", "AI for Beginners", "Data Science Pro")

# Function with **kwargs (keyword arguments)

def student_info(**details):
    print("The student ID is " + details["id"])

student_info(name="Arun", grade="A", id="1023")

def product_info(**item):
    print("The product category is " + item["category"])

product_info(name="Laptop", price="75000", category="Electronics")


# Function that takes a list and prints each item
def show_cart_items(cart):
    for item in cart:
        print(item)

# Example shopping cart
cart_items = ["Laptop", "Headphones", "Mouse"]

# Call the function
show_cart_items(cart_items)
