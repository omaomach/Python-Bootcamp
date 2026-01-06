class Employee:
    company = "Comraid"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self): # This is a dunder method
        return f"My name is {self.name}, an employee of {self.company} and my salary is {self.salary}"
    # These methods allow you to define how your objects interact with built-in Python operators, functions, and language constructs.
    # They provide a way to implement operator overloading and customize the behaviour of a class in a Pythonic way.

    def __repr__(self):
        return f"name: {self.name}\nsalary: {self.salary}"

    def __len__(self):
        return len(self.name)

e = Employee("Kris", 25000)
print(e.name, e.salary)
print(str(e)) # Dunder method in action
print(repr(e))
print(len(e))