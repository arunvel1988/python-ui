# ==========================
# Python: List All String Methods
# ==========================

import pprint

print("=== ALL STRING METHODS IN PYTHON ===\n")

# dir(str) gives all attributes and methods of string
all_methods = dir(str)

# Filter only callable methods (ignore dunder methods if needed)
string_methods = [method for method in all_methods if not method.startswith('__')]

# Pretty print all string methods
pprint.pprint(string_methods)

print("\n=== EXAMPLES OF SOME STRING METHODS ===")

sample = "  hello world  "
print("Original string:", repr(sample))

# Demonstrate a few useful ones
print("Upper:", sample.upper())
print("Lower:", sample.lower())
print("Title:", sample.title())
print("Strip:", sample.strip())
print("Replace 'world' with 'Python':", sample.replace('world', 'Python'))
print("Split:", sample.split())
print("Join:", "-".join(sample.split()))
print("Find 'world':", sample.find('world'))
print("Count 'l':", sample.count('l'))
