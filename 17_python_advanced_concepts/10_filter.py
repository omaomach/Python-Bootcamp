def is_greater_than_9(x):
    if x > 9:
        return True
    else:
        return False

numbers = [1, 2, 3, 5, 6, 10, 13, 14 ,78, 100, 8, 112, 200]

new_numbers = filter(is_greater_than_9, numbers)

print(list(new_numbers))