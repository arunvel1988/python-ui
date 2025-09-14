# List of products in stock
products = ["Mobile", "Tablet", "Smartwatch"]

# Loop through each product and print it
for item in products:
    print(item)



# Loop through each character in a string
for ch in "Arunvel":
    print(ch)


# List of items in cart
cart_items = ["mobile", "laptop", "headphones", "charger"]

for item in cart_items:
    print(item)
    if item == "laptop":
        print("Laptop found in cart. Stopping search.")
        break


# List of products
products = ["tshirt", "discounted_item", "jeans", "shoes"]

for product in products:
    if product == "discounted_item":
        # Skip discounted items
        continue
    print("Processing product:", product)



# Print numbers from 0 to 5
for x in range(6):
    print("Current number is:", x)


# Print numbers starting from 2 up to (but not including) 6
for x in range(2, 6):
    print("Value is:", x)

# Printing product IDs in steps of 4
for product_id in range(101, 130, 4):
    print("Processing Product ID:", product_id)


sizes = ["Small", "Medium", "Large"]
items = ["T-Shirt", "Shoes", "Cap"]

for size in sizes:
    for item in items:
        print("Available:", size, item)


products = ["Laptop", "Phone", "Headphones"]

for item in products:
    pass  # We'll implement processing later

print("Loop finished. (Processing not yet added)")
