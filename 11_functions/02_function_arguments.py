def add(a, b, c=1): # a and b are "parameters"
    sum = a + b + c
    return sum

solution = add(3, 5, 4) # 3 and 5 are "positional arguments, 4 is a default argument"
print(solution)

solution2 = add(b=4, a=7, c=2) # here we have key word arguments
print(solution2)