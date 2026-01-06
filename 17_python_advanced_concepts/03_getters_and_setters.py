class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

employee1 = Employee("Jude Israel", 25)


employee1.projects = 7
print(employee1.projects)
print(employee1.name)