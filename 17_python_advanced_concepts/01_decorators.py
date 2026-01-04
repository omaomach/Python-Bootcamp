# A decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then it returns that new function

def decorator(function):
    def wrapper():
        print("Calling function...")
        function()
        print("Called and executed the function.")
    return wrapper

def say_hello():
    print("Hello")

f = decorator(say_hello)
f()

'''
f will look something like this
def f():
    print("Calling function...")
    print("Hello")
    print("Called and executed the function.")
'''