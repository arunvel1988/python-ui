import re

text = "Order123"

# Find all non-digits
print(re.findall(r"\D", text))
# ['O', 'r', 'd', 'e', 'r']


text = "cart123"

# Find all word characters (letters + digits + _)
print(re.findall(r"\w", text))
# ['c', 'a', 'r', 't', '1', '2', '3']


text = "cart#123"

print(re.findall(r"\W", text))
# ['#']


text = "red green blue"

print(re.findall(r"\s", text))
# [' ', ' ']

