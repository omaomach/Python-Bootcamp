class Employee:

    def __init__(self, salary, name, bond): # The init method is called the constructor. It's automatically run whenever you create a new object from a class
        self.salary = salary # create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond

    def get_salary(self): # self is import because it's a way to reference the object of the class which is being created
        return self.salary

    def get_info(self):
        return f"The name of the employee is {self.name}, salary is ${self.salary} and bond is ${self.bond}"

employee1 = Employee(250000, 'Joel', '5 years')
print(employee1.get_salary())

employee2 = Employee(250000, 'Joash', 'Many years')
print(employee2.get_info())

# It's like saying:
# 1. Create a new Employee object.
# 2. Run the __init__ method on this new object:
#    - Set employee1.salary = 250000
#    - Set employee1.name = "Joel"
#    - Set employee1.bond = "5 years"