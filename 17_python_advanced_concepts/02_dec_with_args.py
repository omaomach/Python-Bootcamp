def repeat(n):
    def decorator(func):
        def wrapper(name):
            for i in range(n):
                func(name)
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello {name}")

# Same as:
'''
say_hello = repeat(3)(say_hello)
#           ↑          ↑
#           │          └── returns wrapper (this becomes the new say_hello)
#           └── returns decorator
# i.e
decorator = repeat(3)
wrapper = decorator(say_hello)
say_hello = wrapper

**Output of `say_hello("Joash")`:**
'''

say_hello("Joash")