t = (12, 15, 18, 12, 19)

print(t.count(12)) # Returns the number of times an element appears in tuple
print(t.index(12)) # Returns the index of the first occurrence of an item in a tuple

## WHY USE TUPLES

# 1. They are faster than lists (since they are immutable)
# 2. Used as dictionary keys (since they are hashable)
# 3. Safe from unintended modification