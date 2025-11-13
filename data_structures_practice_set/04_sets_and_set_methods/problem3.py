a = {1, 2, 3}

b = {3, 4, 5}

c = a.union(b)
print(c)
d = b.union(a)
print(d) # The union of the 2 sets is 3

e = a.intersection(b)
print(e) # The intersection is 3

f = a.difference(b)
print(f) # The elements that are in "a" but not "b" are 1 and 2