import os
import shutil

a = os.listdir("dir") # Get the content of a directory
print(a)
print(os.getcwd())
print(os.path.exists("sub"))
# os.remove("sample.txt") # This can only remove files
os.rmdir("dir") # This can only remove empty directory. if the directory has content. It cant be removed.