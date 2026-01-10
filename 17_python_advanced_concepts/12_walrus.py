# Walrus operator examples
### 1 ###
def very_slow_func():
    print("Something...")
    print("Something...")
    print("Something...")
    print("Something...")
    print("Something...")
    return 7

# if (a := very_slow_func()) > 6:
#     print(a)
#
# else:
#     print("Its not greater than 10")

### 2 ###
# Without walrus operator
# data =  input("Enter a value (or 'q' to exit): ")
#
# while data != 'q':
#     print(f"You entered: {data}")
#     data = input("Enter a value (or 'q' to exit): ")

# With walrus operator
while (data := input("Enter a value (or 'q' to exit): ")) != 'q': # The assignment and condition check happens in one line, making the code cleaner and eliminating the need for initial input() before the loop
    print(f"You entered: {data}")