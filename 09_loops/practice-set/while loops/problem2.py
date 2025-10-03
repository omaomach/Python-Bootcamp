correctpwd = "joashomao"

# while True:
#     pwd = input(f"Enter a password: ")
#     if pwd == correctpwd:
#         print("Access granted")
#         break
#     else:
#         print("Incorrect password. Try again.")

entered_pwd = input("Enter password \n")

while entered_pwd != correctpwd:
    entered_pwd = input("Incorrect! Please try again \n")

print("Access Granted")