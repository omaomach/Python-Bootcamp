def divide(a, b):
    try:
        quotient = a / b
        print(f"{a}/{b} is {quotient}")
        return quotient

    except Exception as e:
        print(e)
        return None

    # This is always executed no matter if try completely executes or not
    # Whenever we have a function returning something, and we want some clean up to happen, put the "clean up" inside finally, and it will always be executed
    finally:
        print("This is always executed")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

divide(a, b)