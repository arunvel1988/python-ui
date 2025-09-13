# ==========================
# Python Lists: Operations & Methods
# ==========================

print("=== LIST DECLARATION ===")
list1 = [1, 2, 3, 4, 5]
list2 = ["Arun", "Meena", "Rahul"]
list3 = [1, "Python", 3.14, True]
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

print("\n=== LIST OPERATIONS ===")
# Indexing
print("First element of list1:", list1[0])
print("Last element of list2:", list2[-1])

# Slicing
print("list1[1:4]:", list1[1:4])
print("list2[:2]:", list2[:2])

# Concatenation
concat = list1 + [6, 7, 8]
print("Concatenation:", concat)

# Repetition
repeat = list2 * 2
print("Repetition:", repeat)

# Membership
print("Is 3 in list1?", 3 in list1)
print("Is 'Python' not in list2?", 'Python' not in list2)

# Length
print("Length of list3:", len(list3))

print("\n=== LIST METHODS ===")
sample = [10, 20, 30, 40, 50]

# append
sample.append(60)
print("append(60):", sample)

# extend
sample.extend([70, 80])
print("extend([70, 80]):", sample)

# insert
sample.insert(2, 25)
print("insert(2, 25):", sample)

# remove
sample.remove(40)
print("remove(40):", sample)

# pop
popped = sample.pop()
print("pop():", popped, "=>", sample)

# clear
sample_copy = sample.copy()
sample_copy.clear()
print("clear():", sample_copy)

# index
print("index of 25:", sample.index(25))

# count
print("count of 20:", sample.count(20))

# sort
sample.sort()
print("sort():", sample)

# reverse
sample.reverse()
print("reverse():", sample)

# copy
sample_copy2 = sample.copy()
print("copy():", sample_copy2)

# Nested list example
nested = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", nested)
print("Access nested[1][0]:", nested[1][0])

print("\n=== LIST COMPREHENSIONS ===")
# Square numbers
squares = [x**2 for x in range(1, 6)]
print("Squares 1-5:", squares)

# Even numbers from a list
evens = [x for x in sample if x % 2 == 0]
print("Even numbers from sample:", evens)
