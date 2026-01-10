# map, filter, and reduce are higher-order functions in Python (and many other programming languages) that operate
# on iterables (lists, tuples, e.t.c).
# They provide a concise and functional way to perform common operations on sequences of data without using explicit loops.

numbers = [1, 2, 3, 45, 41]

squared_numbers = map(lambda x: x * x, numbers) # Please remember, by default, map returns a map object

print(list(squared_numbers)) # Here, we convert the map object to a list