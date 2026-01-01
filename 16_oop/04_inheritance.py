### Inheritance ###
# It's like a family tree. A child class or subclass inherits traits (attributes and methods) from
# its parent class (or superclass)
# This allows you to create new classes that are specialized versions of existing classes, without rewriting all the code

class Animal:
    location = "Australia"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speaking now...")

class Dog(Animal): # The Dog class is extending the Animal class and reusing its methods and attributes
    def speak(self):
        super().speak() # Inside the child class, super() lets you call methods from the parent class.
        # This is useful when you want to extend the parent's behaviour instead of completely replacing it.
        print("Woof")


animal1 = Dog("Spots")
animal1.speak()
print(animal1.location)