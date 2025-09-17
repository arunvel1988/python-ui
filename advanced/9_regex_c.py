import re

text = "hello"

print(re.findall(r"^he", text))   # starts with 'he'
# ['he']

print(re.findall(r"lo$", text))   # ends with 'lo'
# ['lo']



#* → 0 or more

#+ → 1 or more

#? → 0 or 1

#{n} → exactly n times

# {n,m} → between n and m times



text = "he hello hee heee"

print(re.findall(r"he*", text))   # 'h' + 0 or more 'e'
# ['he', 'he', 'hee', 'heee']


text = "Price: 100 USD"

pattern = r"(\d+) USD"
print(re.findall(pattern, text))
# ['100']
