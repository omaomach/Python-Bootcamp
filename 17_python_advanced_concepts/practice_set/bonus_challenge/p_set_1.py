def decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function(s)...")
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

@decorator
def subtract(a, b):
    return a - b

@decorator
def multiply(a, b):
    return a * b

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_details(name="Alice", age=25, city="Delhi")

print(add(1, 2))
print(subtract(1, 2))
print(multiply(12, 2))