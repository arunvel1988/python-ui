# ==========================
# Python Variable Types and Assignments (Unique Examples)
# ==========================

print("=== MULTIPLE ASSIGNMENT ===")
first_fruit, second_fruit, third_fruit = "Mango", "Papaya", "Lychee"
print("first_fruit =", first_fruit)
print("second_fruit =", second_fruit)
print("third_fruit =", third_fruit)

print("\n=== SAME VALUE TO MULTIPLE VARIABLES ===")
score1 = score2 = score3 = 88
print("score1 =", score1, "score2 =", score2, "score3 =", score3)

print("\n=== DIFFERENT DATA TYPES ===")

# Integer
age = 27
print("Integer:", age, type(age))

# Float
temperature = 36.6
print("Float:", temperature, type(temperature))

# String
username = "Arunvel"
print("String:", username, type(username))

# Boolean
is_registered = True
print("Boolean:", is_registered, type(is_registered))

# List
shopping_list = ["Laptop", "Mouse", "Keyboard", 2]
print("List:", shopping_list, type(shopping_list))

# Tuple
coordinates = (12.34, 56.78, 90.12)
print("Tuple:", coordinates, type(coordinates))

# Set
unique_tags = {"python", "flask", "docker", 101}
print("Set:", unique_tags, type(unique_tags))

# Dictionary
user_profile = {"name": "Arunvel", "age": 27, "country": "India"}
print("Dictionary:", user_profile, type(user_profile))

# NoneType
default_value = None
print("NoneType:", default_value, type(default_value))
