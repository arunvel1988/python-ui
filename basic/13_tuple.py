# ==========================
# Python Tuples: Methods & Operations
# ==========================

print("=== ALL TUPLE METHODS ===")
all_methods = dir(tuple)
tuple_methods = [m for m in all_methods if not m.startswith("__")]
print(tuple_methods)

print("\n=== TUPLE DECLARATION ===")
t1 = (1, 2, 3, 4, 5)
t2 = ("Arun", "Meena", "Rahul")
t3 = (1, "Python", 3.14, True)
print("t1:", t1)
print("t2:", t2)
print("t3:", t3)

print("\n=== TUPLE OPERATIONS ===")
# Indexing
print("First element of t1:", t1[0])
print("Last element of t2:", t2[-1])

# Slicing
print("t1[1:4]:", t1[1:4])
print("t2[:2]:", t2[:2])

# Concatenation
concat = t1 + (6, 7, 8)
print("Concatenation:", concat)

# Repetition
repeat = t2 * 2
print("Repetition:", repeat)

# Membership
print("Is 3 in t1?", 3 in t1)
print("Is 'Python' not in t2?", 'Python' not in t2)

# Length
print("Length of t3:", len(t3))

print("\n=== TUPLE METHODS EXAMPLES ===")
sample = (10, 20, 30, 10, 40, 10)

# count
print("count(10):", sample.count(10))

# index
print("index(30):", sample.index(30))

print("\n=== NESTED TUPLES ===")
nested = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested)
print("Access nested[1][0]:", nested[1][0])

print("\n=== TUPLE IMMUTABILITY DEMO ===")
try:
    sample[0] = 100
except TypeError as e:
    print("Error on assignment (immutable):", e)

print("\n=== CONVERT BETWEEN LIST AND TUPLE ===")
# List to tuple
list1 = [1, 2, 3]
t_from_list = tuple(list1)
print("Tuple from list:", t_from_list)

# Tuple to list
tuple1 = (4, 5, 6)
list_from_tuple = list(tuple1)
print("List from tuple:", list_from_tuple)
