class Employee:
    company = 'ACER' # This is a class attribute

    def __init__(self, salary, name, bond, company): # The init method is called the constructor. It's automatically run whenever you create a new object from a class
        self.salary = salary # create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary

    def get_info(self):
        return f"The name of the employee is {self.name}, salary is ${self.salary} and bond is ${self.bond}"

employee1 = Employee(250000, 'Joash', '94', "iBall")
print(employee1.company) # Will always print instance attribute whenever present, else will print class attribute
print(Employee.company) # This will always print the class attribute

# Object Introspection - this is a way in Python, to find out how many methods an object has access to
print(dir(employee1))