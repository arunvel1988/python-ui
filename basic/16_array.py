# =======================================
# Arrays in Python (using Lists & array module)
# =======================================

import array

print("=== ARRAYS USING LIST (MOST COMMON) ===")
arr = [10, 20, 30, 40, 50]
print("Array (List):", arr)

# Access
print("First Element:", arr[0])
print("Last Element:", arr[-1])

# Update
arr[1] = 25
print("After Updating index 1:", arr)

# Append
arr.append(60)
print("append(60):", arr)

# Insert
arr.insert(2, 35)
print("insert(2, 35):", arr)

# Remove
arr.remove(40)
print("remove(40):", arr)

# Pop
popped = arr.pop()
print("pop() ->", popped, "Remaining:", arr)

# Slice
print("arr[1:3]:", arr[1:3])

# Loop
print("Looping:", end=" ")
for x in arr:
    print(x, end=" ")
print("\n")


print("=== ARRAYS USING array MODULE (TYPE RESTRICTED) ===")
# i = integer, f = float
arr_int = array.array('i', [1, 2, 3, 4, 5])
print("Integer Array:", arr_int)

arr_float = array.array('f', [1.1, 2.2, 3.3])
print("Float Array:", arr_float)

# Operations
arr_int.append(6)
print("append(6):", arr_int)

arr_int.extend([7, 8, 9])
print("extend([7,8,9]):", arr_int)

arr_int.remove(2)
print("remove(2):", arr_int)

print("Index of 4:", arr_int.index(4))
print("Count of 3:", arr_int.count(3))

print("Slice arr_int[2:5]:", arr_int[2:5])

print("Convert to list:", arr_int.tolist())
print()


print("=== ARRAYS USING STRINGS (CHAR ARRAY) ===")
arr_char = array.array('u', ['A', 'r', 'u', 'n'])
print("Char Array:", arr_char)
print("Joined String:", "".join(arr_char))

