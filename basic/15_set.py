# ==========================
# Python Sets: Methods & Operations
# ==========================

print("=== ALL SET METHODS ===")
all_methods = dir(set)
set_methods = [m for m in all_methods if not m.startswith("__")]
print(set_methods)

print("\n=== SET DECLARATION ===")
set1 = {1, 2, 3, 4, 5}
set2 = {"Arun", "Meena", "Rahul"}
set3 = set([1, 2, 3, 4])
print("set1:", set1)
print("set2:", set2)
print("set3:", set3)

print("\n=== SET OPERATIONS ===")
# Membership
print("Is 3 in set1?", 3 in set1)
print("Is 'Python' not in set2?", 'Python' not in set2)

# Add element
set1.add(6)
print("add(6):", set1)

# Remove element
set1.remove(4)  # raises KeyError if not present
print("remove(4):", set1)

# discard (safe remove)
set1.discard(10)  # no error if element not present
print("discard(10):", set1)

# pop
popped = set1.pop()  # removes arbitrary element
print("pop():", popped, "=>", set1)

# clear
set_copy = set1.copy()
set_copy.clear()
print("clear():", set_copy)

print("\n=== SET METHODS ===")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# union
print("A.union(B):", A.union(B))

# intersection
print("A.intersection(B):", A.intersection(B))

# difference
print("A.difference(B):", A.difference(B))

# symmetric_difference
print("A.symmetric_difference(B):", A.symmetric_difference(B))

# isdisjoint
print("A.isdisjoint(B):", A.isdisjoint(B))

# issubset & issuperset
print("A.issubset(B):", A.issubset(B))
print("A.issuperset(B):", A.issuperset(B))

print("\n=== FROZEN SET ===")
fset = frozenset([1, 2, 3, 4])
print("frozenset:", fset)
# fset.add(5) # Not allowed, immutable
