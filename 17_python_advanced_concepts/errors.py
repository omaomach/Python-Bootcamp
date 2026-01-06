while True:
    try:
        a = int(input("Enter a number 1: "))
        b = int(input("Enter a number 2: "))

        quotient = a / b

        print(f"{a}/{b} is {quotient}")

    except ValueError:
        print("Please input a number.")

    except ZeroDivisionError:
        print("You can't divide by zero.")

    except Exception as e:
        print("Something went wrong", e) # Whenever there is an error, the code inside the except block is run