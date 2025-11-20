class Animal:
    location = "Australia"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speaking now...")

class Dog(Animal):
    def speak(self):
        super().speak() # Inside the child class, super() lets you call methods from the parent class.
        # This is useful when you want to extend the parent's behaviour instead of completely replacing it.
        print("Woof")


animal1 = Dog("Spots")
animal1.speak()
print(animal1.location)