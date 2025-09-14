# Lambda to add tax (10 currency units) to the product price
add_tax = lambda price: price + 10

print("Final price of the product:", add_tax(90))
print("/n/n")

# Lambda to calculate total price of items (price × quantity)
total_cost = lambda price, quantity: price * quantity

print("Total cost:", total_cost(500, 3))   # 500 per item, quantity 3
