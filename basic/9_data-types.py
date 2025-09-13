# ==========================
# Python Data Types Demo
# ==========================

print("=== TEXT TYPE ===")
text_var = "Arunvel"
print("Value:", text_var, "| Type:", type(text_var))

print("\n=== NUMERIC TYPES ===")
int_var = 42
float_var = 3.1415
complex_var = 2 + 3j
print("Integer:", int_var, "| Type:", type(int_var))
print("Float:", float_var, "| Type:", type(float_var))
print("Complex:", complex_var, "| Type:", type(complex_var))

print("\n=== SEQUENCE TYPES ===")
list_var = [10, 20, 30, "Python"]
tuple_var = (1, 2, 3, "Arun")
range_var = range(5)
print("List:", list_var, "| Type:", type(list_var))
print("Tuple:", tuple_var, "| Type:", type(tuple_var))
print("Range:", list(range_var), "| Type:", type(range_var))

print("\n=== MAPPING TYPE ===")
dict_var = {"name": "Arun", "age": 27, "city": "Pune"}
print("Dictionary:", dict_var, "| Type:", type(dict_var))

print("\n=== SET TYPES ===")
set_var = {1, 2, 3, "Python"}
frozenset_var = frozenset([4, 5, 6])
print("Set:", set_var, "| Type:", type(set_var))
print("FrozenSet:", frozenset_var, "| Type:", type(frozenset_var))

print("\n=== BOOLEAN TYPE ===")
bool_var = True
print("Boolean:", bool_var, "| Type:", type(bool_var))

print("\n=== BINARY TYPES ===")
bytes_var = b"Hello"
bytearray_var = bytearray([65, 66, 67])
memoryview_var = memoryview(bytearray_var)
print("Bytes:", bytes_var, "| Type:", type(bytes_var))
print("ByteArray:", bytearray_var, "| Type:", type(bytearray_var))
print("MemoryView:", memoryview_var, "| Type:", type(memoryview_var))

print("\n=== NONE TYPE ===")
none_var = None
print("NoneType:", none_var, "| Type:", type(none_var))
