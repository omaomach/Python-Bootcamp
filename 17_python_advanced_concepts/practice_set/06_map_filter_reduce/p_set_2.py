numbers = [10, 11, 12, 13, 14]

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

even = list(filter(is_even, numbers))
print(even)