student = {"name": "Alice", "age": 21, "grade": "A"}

print(student["name"])
student["age"] = 22
print(student["age"])
student["city"] = "New York"
print(student["city"])
print(student.keys())
print(student.values())
print(student.items())
student.pop("age")
print(student)
student.clear()
print(student)