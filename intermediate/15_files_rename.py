
import os


cwd = os.getcwd()
print("Working in:", cwd)


for i in range(3):
    with open(f"file_{i}.txt", "w") as f:
        f.write("Hello student!")

for fname in os.listdir(cwd):
    if fname.endswith(".txt"):
        new_name = fname.replace(".txt", ".bak")
        os.rename(fname, new_name)
        print(f"Renamed: {fname} → {new_name}")
