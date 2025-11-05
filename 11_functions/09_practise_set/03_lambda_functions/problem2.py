my_list = []
for i in range(1, 6):
    my_list.append(i)
print(my_list)

squared = list(map(lambda x: x**2, my_list))
print(squared)

