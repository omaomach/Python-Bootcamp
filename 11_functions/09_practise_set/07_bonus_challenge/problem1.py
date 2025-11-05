# Write a recursive function fibonacci(n) that prints the first n Fibonacci
# numbers.

## ITERATIVE APPROACH
# def fibonacci(n):
#     a, b = 0, 1 # a = current Fibonacci number (starts at 0), b = next Fibonacci number (starts at 1)
#
#     for i in range(n): # repeat the loop n times to print n Fibonacci numbers
#         print(a, end="") # print the current Fibonacci number "a", end=" " keeps output on the same line with a space
#         a, b = b, a + b # both variables are updated simultaneously i.e new a = old b (move to next number), new b = old a + old b
#     print() # print new line at end
#
# fibonacci(6)

## RECURSIVE APPROACH
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = 10

for i in range(n):
    print(fib(i), end=" ")