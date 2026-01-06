class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def first_name(self):
        return self.name.split(" ")[0]

    @first_name.setter
    def first_name(self, first):
        names = self.name.split(" ")
        new_full_name = f"{first} {names[1]}"
        self.name = new_full_name

# To make an attribute read-only, define just the @property decorator (the getter) and leave out the @name.setter method.
# Trying to set the attribute will result in an AttributeError

    # without property definition
    '''
        def set_first_name(self, first):
        names = self.name.split(" ")
        new_full_name = f"{first} {names[1]}"
        self.name = new_full_name
    '''

employee1 = Employee("Jude Israel", 25)

print(employee1.first_name) # first_name is a function, but it looks like a property because we are using a property decorator
employee1.first_name = "Julia"
print(employee1.first_name)

# Without getters and setters
'''
print(employee1.first_name())
employee1.set_first_name("Joash")
print(employee1.first_name())
employee1.projects = 7
print(employee1.projects)
print(employee1.name)
'''