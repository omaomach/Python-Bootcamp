def add(*args): # args will be a tuple of all the values passed to add
    total = 0
    for arg in args:
        total += arg
    return total

print(add(3, 4, 10))