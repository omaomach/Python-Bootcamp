# def sum_of_digits(n):
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n = n // 10
#     return sum
#
# print(sum_of_digits(0))
# print(sum_of_digits(123))

def sum_of_digits(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0

    # Recursive case: last digit + sum of remaining digits
    return (n % 10) + sum_of_digits(n//10)

print(sum_of_digits(123))

"""
## **How it works:**

**Base case:** When `n` reaches 0, there are no more digits, so return 0.

**Recursive case:** 
- Get the last digit with `n % 10`
- Add it to the sum of the remaining digits `sum_digit(n // 10)`

## **Example walkthrough with n = 123:**
```
sum_digit(123)
  = 3 + sum_digit(12)
      = 2 + sum_digit(1)
          = 1 + sum_digit(0)
              = 0

Now unwinding:
  = 1 + 0 = 1
  = 2 + 1 = 3
  = 3 + 3 = 6
  
The recursive version is more elegant but uses more memory (call stack) compared to the iterative version. For very large numbers, the iterative approach is more efficient!
  
"""

