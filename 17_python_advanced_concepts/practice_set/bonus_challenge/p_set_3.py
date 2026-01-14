import logging

logging.basicConfig(level=logging.ERROR)

class InvalidUserInputError(Exception):
    def __init__(self, value, message="Incorrect password"):
        self.value = value
        self.message = message
        super().__init__(self.message)

def get_user_password(prompt):
    while True:
        value = input(prompt)
        try:
            if value != "joash":
                raise InvalidUserInputError(value)
            else:
                return value
        except InvalidUserInputError as e:
            logging.error(f"{e.message}: '{e.value}'")
            print(e.message)

user_password = get_user_password("Please enter your password: ")
print(user_password)