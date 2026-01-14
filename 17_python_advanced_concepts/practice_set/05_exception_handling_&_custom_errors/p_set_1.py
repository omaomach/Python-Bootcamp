class NegativeNumberError(Exception):
    def __init__(self, value, message="Negative numbers are not allowed"):
        self.value = value
        self.message = f"{message}: {value}"
        super().__init__(self.message)

def get_valid_number(prompt):
    while True:
        value = input(prompt)
        try:
            num = int(value)
            if num < 0:
                raise NegativeNumberError(num)
            return num
        except ValueError:
            print("Please input a number.")
        except NegativeNumberError as e:
            print(e.message)

def get_valid_divisor(prompt):
    while True:
        value = input(prompt)
        try:
            num = int(value)
            if num < 0:
                raise NegativeNumberError(num)
            return num
        except ValueError:
            print("Please input a number.")
        except NegativeNumberError as e:
            print(e.message)

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("You can't divide by zero.")
        return None

user_input = get_valid_number("Enter a number: ")
user_input2 = get_valid_divisor("Enter a number: ")

result = divide(user_input, user_input2)
print(result)
