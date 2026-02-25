import shutil
import os

# 1. Copy a file from one folder to another
os.makedirs("backup", exist_ok=True)
shutil.copy("file1.txt", "backup/file1.txt")

# 2. Move a file to a new folder
os.makedirs("archive", exist_ok=True)
shutil.move("file2.txt", "archive/file2.txt")

# 3. Delete a file (irreversible!)
os.remove("archive/file2.txt")