marks = [5, 2, 21, 5, 7]
extra_marks = [11, 14, 17]

print(marks)
marks.append(63) # This will change the original list. Adds the new element at the very end of the list
print(marks)
marks.pop()
print(marks) # Removes the last element in a list
marks.insert(2, 8)
print(marks)
marks.extend(extra_marks)
print(marks)
marks.remove(5)
print(marks)
marks.reverse()
print(marks)
marks.sort()
print(marks)