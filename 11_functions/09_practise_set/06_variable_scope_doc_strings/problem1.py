def increment():
    counter = 0
    counter += 1
    print(f"Counter Value: {counter}")
    return counter

print("Call 1:")
increment()
print("Call 2:")
increment()
print("Call 3:")
increment()
print("Call 4:")
increment()

# The value does NOT persist across function calls! Each time you call increment(), the counter variable is re-initialized to 0, the incremented to 1
# Local variables are created when the function is called and destroyed when it returns. They don't "remember" their previous values

## SOLUTION TO MAKE IT PERSIST
counter = 0

def increment():
    global counter
    counter += 1
    print(f"Counter Value: {counter}")

increment()
increment()
increment()