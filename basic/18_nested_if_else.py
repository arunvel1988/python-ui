

# Example 1: Check if a number is positive, negative, or zero
num = 5

if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")

print("---------------------------------")

# Example 2: Nested check for even/odd after checking positive/negative
num = -4

if num >= 0:
    print("Number is positive")
    if num % 2 == 0:
        print("Number is also even")
    else:
        print("Number is also odd")
else:
    print("Number is negative")
    if num % 2 == 0:
        print("Number is also even")
    else:
        print("Number is also odd")

print("---------------------------------")

# Example 3: Nested if to find the largest of three numbers
a = 25
b = 40
c = 30

if a > b:
    if a > c:
        print("a is the largest:", a)
    else:
        print("c is the largest:", c)
else:
    if b > c:
        print("b is the largest:", b)
    else:
        print("c is the largest:", c)

print("---------------------------------")

# Example 4: Grading system with nested if
marks = 85

if marks >= 50:
    print("Student passed")
    if marks >= 90:
        print("Grade: A+")
    elif marks >= 75:
        print("Grade: A")
    elif marks >= 60:
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("Student failed")

print("---------------------------------")