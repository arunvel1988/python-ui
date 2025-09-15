import os

cwd = os.getcwd()
print("Current Working Directory:", cwd)

filename = os.path.join(cwd, "notes.txt")

if os.path.exists(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        print(f"The file '{filename}' has {len(lines)} lines.")
else:
    print(f"File 'notes.txt' not found in {cwd}")
