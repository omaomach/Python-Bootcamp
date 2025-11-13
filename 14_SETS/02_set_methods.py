s = {34, 23, 13, 1, 20}

print(s)
s.add(42)
s.add(20) # you cannot add a number that already exists in a set
s.remove(1) # In the case the element to be removed is not found, this will throw and error
s.discard(44) # This does not throw an error in the case that the element to be removed is not found
s.pop() # Removes a random element from a set
print(s)