# When you look at the previous method of reading from files, you'll notice that we have to close the file each time at the very end.
# Sometimes you might forget this, thus the reason as to why we have the "with" statement
# "with", ensures that the file is automatically closed, even if an error occurs

try:
    with open('joash.txt', "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
    with open("joash.txt", "w") as file: # remember, when using write "w", if the file you are writing to has data, the data will be overwritten.
        file.write("Data written using 'with'.\n")
        # No need to write f.close() because file is already closed by default when using with syntax