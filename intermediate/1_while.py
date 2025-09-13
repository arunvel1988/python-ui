
##################
num = 1
while num <= 10:
    print("Number:", num)
    num = num + 1

print("Finished counting 1 to 10")


##########################



count = 5
while count > 0:
    print("Countdown:", count)
    count = count - 1

print("Blast Off!")

##########################
# Example 3: Sum of numbers until n

n = 5
total = 0
i = 1

while i <= n:
    total = total + i
    i = i + 1

print("Sum of first", n, "numbers is:", total)
##########################

# Example 5: Stop loop when condition met

num = 1
while True:   # infinite loop
    print("Number:", num)
    if num == 5:
        print("Breaking loop at 5")
        break
    num = num + 1
############################

# Example 6: Skip even numbers

num = 0
while num < 10:
    num = num + 1
    if num % 2 == 0:
        continue
    print("Odd number:", num)

#####################################

# Example 7: Simple e-commerce cart using while loop

cart = []
while True:
    item = input("Add item to cart (or type 'checkout'): ")
    if item.lower() == "checkout":
        break
    cart.append(item)

print("Your cart contains:", cart)
print("Thank you for shopping!")
###################