### Class ###
# Think of a class as a blueprint or a template.
# It defines what an object will be like - what data it will hold and what actions in can perform.
# It doesn't create the object its, but holds the information dictating how the object should be

### Object ###
# An object is a specific instance created from the class blueprint
# Each object has its own unique set of data

class Employee:
    company = 'COMRAID'

    def get_salary(self): # In a class, self is like saying "this particular object" i.e joash and joel. It's a way to reference an object of the class
        # self is always the first parameter on a method definition in a class.
        # Python handles it automatically when you call the method i.e you don't type self when calling the method; Python inserts it for you.
        return 200000

joash = Employee()
print(joash.get_salary())

joel = Employee()
print(joel.get_salary())
print(joash.company)