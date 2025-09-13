rows = 5
for i in range(1, rows + 1):
    print("*" * i)
print("Finished printing pattern")

# Add two blank lines between patterns
print("\n\n")

for i in range(rows, 0, -1):
    print("*" * i)
print("Finished printing reverse pattern")
print("\n\n")

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)
print("Finished printing right-aligned pattern")
print("\n\n")

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
print("Finished printing pyramid pattern")
print("\n\n")

rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
print("Finished printing reverse pyramid pattern")
print("\n\n")


rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
print("Finished printing diamond pattern")
print("\n\n")

rows = 5
for i in range(rows):
    print("* " * rows)
print("Finished printing square pattern")
print("\n\n") 

rows = 5
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("Finished printing hollow square pattern")
print("\n\n")


