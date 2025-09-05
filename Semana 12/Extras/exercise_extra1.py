class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary > 0:
            self._salary = salary
        else:
            print("The salary cannot be negative")

    def promote(self, percentage):
        self._salary += self.salary * percentage


employee = Employee("Laura", 1000)
employee.promote(0.1)

print(employee.salary)
