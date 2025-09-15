from ecomm_tools import file_tools, price_tools

print("Files:", file_tools.list_files("."))

price = 1000
print("Discounted Price:", price_tools.apply_discount(price, 10))  # 900
