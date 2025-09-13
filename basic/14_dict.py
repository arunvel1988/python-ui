# ==========================
# Python Dictionaries: Methods & Operations
# ==========================

print("=== ALL DICTIONARY METHODS ===")
all_methods = dir(dict)
dict_methods = [m for m in all_methods if not m.startswith("__")]
print(dict_methods)

print("\n=== DICTIONARY DECLARATION ===")
dict1 = {"name": "Arun", "age": 27, "city": "Pune"}
dict2 = {1: "Python", 2: "Java", 3: "C++"}
dict3 = {"fruits": ["apple", "banana"], "numbers": [1,2,3]}
print("dict1:", dict1)
print("dict2:", dict2)
print("dict3:", dict3)

print("\n=== DICTIONARY OPERATIONS ===")
# Access values
print("dict1['name']:", dict1["name"])
print("dict3['fruits'][1]:", dict3["fruits"][1])

# Keys, Values, Items
print("dict1.keys():", dict1.keys())
print("dict1.values():", dict1.values())
print("dict1.items():", dict1.items())

# Membership
print("'age' in dict1:", 'age' in dict1)
print("'Arun' in dict1:", 'Arun' in dict1)

print("\n=== DICTIONARY METHODS EXAMPLES ===")
sample = {"a": 10, "b": 20, "c": 30}

# get
print("get('b'):", sample.get("b"))

# update
sample.update({"d": 40})
print("update({'d': 40}):", sample)

# pop
popped = sample.pop("a")
print("pop('a'):", popped, "=>", sample)

# popitem
popped_item = sample.popitem()
print("popitem():", popped_item, "=>", sample)

# setdefault
res = sample.setdefault("e", 50)
print("setdefault('e', 50):", res, "=>", sample)

# copy
sample_copy = sample.copy()
print("copy():", sample_copy)

# clear
sample_copy.clear()
print("clear():", sample_copy)

# fromkeys
new_dict = dict.fromkeys(["x", "y", "z"], 0)
print("fromkeys(['x','y','z'], 0):", new_dict)

print("\n=== NESTED DICTIONARIES ===")
nested_dict = {
    "person1": {"name": "Arun", "age": 27},
    "person2": {"name": "Meena", "age": 25}
}
print("nested_dict:", nested_dict)
print("Access nested_dict['person1']['name']:", nested_dict["person1"]["name"])
