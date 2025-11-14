my_list = [1, 2, 3, 3, 5, 7, 8, 8]

def duplicates_remover(list):
    my_set = set(list)
    return my_set

print(duplicates_remover(my_list))