coordinates = (10, 20)

print(coordinates)

# coordinates[0] = 50 # Tuples dont support object assigment or modification
print(coordinates)

coordinates_list = list(coordinates)
coordinates_list[0] = 50

coordinates = tuple(coordinates_list)
print(coordinates)

# The original tuple "coordinates" cannot be changed. Tuples cannot be changed