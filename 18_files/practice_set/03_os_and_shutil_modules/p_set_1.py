import os

# 1. Print the current working directory
print(os.getcwd())

# 2. List all files and folders in the cirrent directory
print(os.listdir("18_files"))

# 3. Create a new folder "my_folder". The folder will be created inside the current working directory
os.makedirs("my_folder", exist_ok=True) # prevents the code from throwing a FileExistsError if my_folder already exists. Without it, running the script a second time would crash. It's a safety measure — if the folder is already there, it just moves on silently.