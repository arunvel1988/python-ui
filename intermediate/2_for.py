

for num in range(1, 6):
    print("Number:", num)

print("Finished looping 1 to 5")
##########################


fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print("Fruit:", fruit)
print("Finished listing fruits")
##########################



colors = ["red", "green", "blue"]

for i in range(len(colors)):
    print("Index:", i, "Color:", colors[i])
print("Finished listing colors")
##########################



word = "Python"

for ch in word:
    print("Character:", ch)
print("Finished iterating string")
##########################
for num in range(1, 11):
    if num % 2 == 0:
        print("Even:", num)
print("Finished printing even numbers")
##########################



for i in range(1, 6):
    for j in range(1, 6):
        print(i, "x", j, "=", i*j)
    print("-----")
print("Finished multiplication tables")
##########################



for num in range(1, 11):
    if num == 5:
        print("Breaking at:", num)
        break
    print("Number:", num)
print("Finished loop with break")
##########################
# 


for num in range(1, 11):
    if num % 3 == 0:
        continue
    print("Number:", num)
print("Finished loop with continue") 
##########################

# Example 9: Loop through dictionary items

student = {"name": "Arun", "age": 22, "course": "Python"}

for key, value in student.items():
    print(key, ":", value)
print("Finished iterating dictionary")
##########################

# Example 10: Process a list of orders

orders = ["Laptop", "Mobile", "Shoes", "Watch"]

for order in orders:
    print("Processing order:", order)

print("All orders processed")
##########################
