import re

text = "apple mango banana apricot"

# Find exact word
print(re.findall("apple", text))
# ['apple']


text = "cat bat rat mat"

# Match any word starting with c, b or r
print(re.findall(r"[cbr]at", text))
# ['cat', 'bat', 'rat']



text = "I bought 3 apples and 5 mangoes."
pattern = r"\d"   # \d means digit

print(re.findall(pattern, text))  
# ['3', '5']

