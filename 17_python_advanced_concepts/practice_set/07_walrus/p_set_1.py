while True:
    user_input = input("Type something awesome or type 'quit' to exit: ")
    print(user_input)
    if prompt := user_input.lower() == "quit":
        break