class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method (default)
    def print_info(self):
        info = f"Name: {self.name}\nSalary: {self.salary}"
        print(info)

    # Static Method
    @staticmethod
    def sum(a, b, c): # This is a method that doesn't require self and self is not automatically passed when the function is called. Used for righting utility methods
        return a  + b + c

    # Class Methods
    @classmethod
    def print_company(cls):
        company = cls.company
        print(company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Bridget", 100000)
e2 = Employee("Kris", 200000)
print(Employee.company)
# print(Employee.name) # You cant do this because name is an instance attribute, will throw an error
e1.print_info()
e2.print_info()

print(e1.sum(2,3,5))

e2.print_company()
e2.change_company("Lenovo")
e2.print_company()
print(Employee.company) # The class variable has been changed

# Whenever an attribute is called, inside an object, its first searched within its instance attributes, if not found, it's searched in the class attributes