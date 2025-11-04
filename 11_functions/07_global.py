def sum(a, b):
    print("Hey I am summing...")
    c = a + b
    global z # to modify a global variable inside a function use the "global" keyword
    z = 0 # This will now refer to global z and not create a local variable
    return c

z = 9

print(z)
print(sum(3, 18))
print(z)