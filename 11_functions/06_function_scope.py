# In Python, variable have scope (where they can be accessed) and lifetime (how long they exist)
# Variables are created when a function is called and destroyed when it returns.

def sum(a, b):
    # a and b are local variables
    c = a + b
    y = 1 # this creates a local variable called y which is destroyed after this function returns.
    return c # A function only keeps a variable until it returns

def greet():
    z = 33 # Local variable
    print("Joash")

y = 8 # y is a global variable

print(sum(3, 4))
greet()