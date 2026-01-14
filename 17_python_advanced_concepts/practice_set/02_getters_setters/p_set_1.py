class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

employee = Employee(300000)
print(employee.salary)

# employee.salary = -1000000
# print(employee.salary)

employee.salary = 1000000
print(employee.salary)