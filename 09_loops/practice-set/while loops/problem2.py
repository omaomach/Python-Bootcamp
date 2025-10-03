correctpwd = "joashomao"

while True:
    pwd = input(f"Enter a password: ")
    if pwd == correctpwd:
        print("Access granted")
        break
    else:
        print("Incorrect password. Try again.")