try:
    f = open("notes.txt", "r")
    content = f.read()
    print(content)
    f.close()
except FileNotFoundError:
    print("File not found")