class Employee:
    def __init__(self):
        self._salary = 300000

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = salary

employee = Employee()
print(employee.salary)

# employee.salary = -1000000
# print(employee.salary)

employee.salary = 1000000
print(employee.salary)