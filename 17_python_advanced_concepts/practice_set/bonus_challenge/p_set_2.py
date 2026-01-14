class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __iter__(self):
        yield self.x
        yield self.y

vector = Vector(1, 2)
vector2 = Vector(3, 4)
vector3 = vector + vector2
print(list(vector3))