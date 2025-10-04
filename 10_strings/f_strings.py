# String formatting

template = "Dear {}, you are awesome, please help me build this billion dollar company alongside {}"

a = "Python"
a1 = 10000
b = "Node Js"
b1 = 5000
c = "JavaScript"
c1 = 1000

s1 = template.format(a, c)
print(s1)

print(f"Dear {a}, you are worth {a1} and {b}, you are worth {5000}")