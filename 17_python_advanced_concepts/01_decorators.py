# A decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then it returns that new function

def decorator(function):
    def wrapper():
        print("Calling function...")
        function()
        print("Called and executed the function.")
    return wrapper

### The decorator pattern ###
# Wrapper - It wraps the original function with additional behavior
# Higher-order function - it takes a function as input and returns a new function
# Function transformer - it transforms one function into another

@decorator # this is a syntactic sugar for function wrapping/replacement
def say_hello():
    print("Hello")

say_hello()
# f = decorator(say_hello)
# f()

'''
f will look something like this
def f():
    print("Calling function...")
    print("Hello")
    print("Called and executed the function.")
'''