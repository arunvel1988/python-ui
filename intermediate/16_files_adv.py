# organize_files.py
import os
import shutil

cwd = os.getcwd()
print("Organizing files in:", cwd)

# Create some dummy files
open("report.pdf", "w").close()
open("photo.jpg", "w").close()
open("notes.txt", "w").close()

# Define target folders
folders = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".txt": "TextFiles"
}

# Move files
for fname in os.listdir(cwd):
    for ext, folder in folders.items():
        if fname.endswith(ext):
            if not os.path.exists(folder):
                os.mkdir(folder)
            shutil.move(fname, os.path.join(folder, fname))
            print(f"Moved {fname} → {folder}/")
