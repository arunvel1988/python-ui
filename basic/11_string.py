# ==========================
# Python: Remaining String Methods Examples
# ==========================

sample = "  Hello123 World!  "

print("Original string:", repr(sample))

# capitalize
print("\ncapitalize():", sample.capitalize())

# casefold (aggressive lowercasing for comparisons)
print("casefold():", sample.casefold())

# center
print("center(30, '*'):", sample.center(30, '*'))

# encode
print("encode():", sample.encode())

# endswith
print("endswith('!  '):", sample.endswith('!  '))

# expandtabs
tab_sample = "Hello\tWorld"
print("expandtabs(4):", tab_sample.expandtabs(4))

# format
name = "Arun"
age = 27
print("format():", "Name: {}, Age: {}".format(name, age))

# format_map
person = {"name": "Arun", "age": 27}
print("format_map():", "Name: {name}, Age: {age}".format_map(person))

# index & rindex
print("index('World'):", sample.index("World"))
print("rindex('l'):", sample.rindex("l"))

# isalnum, isalpha, isascii, isdecimal, isdigit, isnumeric
print("isalnum():", sample.isalnum())
print("isalpha():", sample.isalpha())
print("isascii():", sample.isascii())
print("isdecimal():", "123".isdecimal())
print("isdigit():", "123".isdigit())
print("isnumeric():", "123".isnumeric())

# isidentifier
print("isidentifier():", "var_1".isidentifier())

# islower, isupper, istitle
print("islower():", sample.islower())
print("isupper():", sample.isupper())
print("istitle():", sample.istitle())

# ljust, rjust
print("ljust(25, '-'):", sample.ljust(25, '-'))
print("rjust(25, '-'):", sample.rjust(25, '-'))

# lstrip, rstrip
print("lstrip():", sample.lstrip())
print("rstrip():", sample.rstrip())

# maketrans + translate
table = str.maketrans("Helo", "1234")
print("translate():", sample.translate(table))

# removeprefix & removesuffix
text = "HelloPythonWorld"
print("removeprefix('Hello'):", text.removeprefix("Hello"))
print("removesuffix('World'):", text.removesuffix("World"))

# rfind
print("rfind('l'):", sample.rfind('l'))

# rpartition, partition
print("partition('123'):", "abc123xyz".partition("123"))
print("rpartition('123'):", "abc123xyz123".rpartition("123"))

# rsplit, splitlines
multi_line = "Line1\nLine2\nLine3"
print("rsplit():", sample.rsplit())
print("splitlines():", multi_line.splitlines())

# startswith
print("startswith('  He'):", sample.startswith("  He"))

# swapcase
print("swapcase():", sample.swapcase())

# translate (example already done with maketrans above)

# zfill
print("zfill(20):", sample.zfill(20))
