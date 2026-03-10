try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("What kind of operation do you want to perform. Press + for addition\nPress - for subtraction\n Press / for division\n Press * for multiplication")

    o = input("Enter Operation: ")

    match o:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "/":
            print(f"The result is: {a / b}")
        case "*":
            print(f"The result is: {a * b}")

except Exception:
    print("Enter a value of a and b")