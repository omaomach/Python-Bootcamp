num1 = int(input(f"Enter first number: "))
num2 = int(input(f"Enter second number: "))
operation = input (f"Choose an operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("Select one of the given operations")