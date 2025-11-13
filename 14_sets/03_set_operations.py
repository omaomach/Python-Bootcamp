a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

c = a.union(b) # c will contain all the elements in a and b, and no duplicates will be allowed
print(c)

d = a.intersection(b) # d will contain the elements that are in both a and b that is 23 and 1
print(d)

e = a.difference(b) # this will give the elements that are in "a" but not in "b". The order matters
print(e)

# Sets are great for eliminating duplicate values