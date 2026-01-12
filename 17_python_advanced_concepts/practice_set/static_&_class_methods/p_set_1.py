class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        return "This is a utility class for math operations."

print(MathUtils.add(1,2))
print(MathUtils.description())