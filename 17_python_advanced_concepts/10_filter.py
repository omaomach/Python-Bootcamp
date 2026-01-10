def is_greater_than_9(x):
    if x > 9:
        return True
    else:
        return False

numbers = [1, 2, 3, 5, 6, 10, 13, 14 ,78, 100, 8, 112, 200]

new_numbers = filter(lambda x: x > 9, numbers) # the is_greater_than_9 method is individually run on all the numbers in the "numbers array". When new returns True, "new_numbers" will collect that number

print(list(new_numbers)) # type cast the filter object to a list then print