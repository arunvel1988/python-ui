# =======================================
# Comparison Operators with IF-ELSE
# =======================================

a = 10
b = 20

print("a =", a, "b =", b)

# Equals
if a == b:
    print("a == b -> Yes, they are equal")
else:
    print("a == b -> No, they are not equal")

# Not Equals
if a != b:
    print("a != b -> Yes, they are different")
else:
    print("a != b -> No, they are the same")

# Less than
if a < b:
    print("a < b -> Yes, a is smaller than b")
else:
    print("a < b -> No, a is not smaller")

# Less than or equal to
if a <= b:
    print("a <= b -> Yes, a is smaller or equal to b")
else:
    print("a <= b -> No, a is greater")

# Greater than
if a > b:
    print("a > b -> Yes, a is greater than b")
else:
    print("a > b -> No, a is not greater")

# Greater than or equal to
if a >= b:
    print("a >= b -> Yes, a is greater or equal to b")
else:
    print("a >= b -> No, a is smaller")

print()
print("Comparison operators always return True/False and are used in decision-making.")
print("Commonly used in if-else statements and loops.")