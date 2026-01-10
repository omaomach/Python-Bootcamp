from functools import reduce

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#   [3, 3, 4, 5, 6, 7, 8, 9]
#   [6, 4, 5, 6, 7, 8, 9]
#   [10, 5, 6, 7, 8, 9]
#   [15, 6, 7, 8, 9]
#   [21, 7, 8, 9]
#   [28, 8, 9]
#   [36, 9]
#   [45]

def sum(x, y):
    return x + y

c = reduce(sum, a)
print(c)

