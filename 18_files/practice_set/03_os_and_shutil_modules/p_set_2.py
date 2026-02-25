import shutil
import os

# 1. Copy a file from one folder to another
os.makedirs("backup", exist_ok=True)
shutil.copy("file1.txt", "backup/file1.txt")

