class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name)
        print(self.age)

mwabe = Person("Mwabe", 21)
mwabe.print_info()