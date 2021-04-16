from operator import attrgetter

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return "{}-{}-{}".format(self.name, self.age, self.salary)


e1 = Employee("ABC", 25, 700)
e2 = Employee("XYZ", 55, 7000)
e3 = Employee("DEF", 65, 70)

lstEmp = [e1, e2, e3]

print("List of Employees        : ", lstEmp)

sortedLstEmp = sorted(lstEmp, key=attrgetter("name"))
print("Sorted list of Employees (Name)          : ", sortedLstEmp)

sortedLstEmp = sorted(lstEmp, key=attrgetter("age"))
print("Sorted list of Employees (Age)           : ", sortedLstEmp)

sortedLstEmp = sorted(lstEmp, key=attrgetter("salary"))
print("Sorted list of Employees (Salary)        : ", sortedLstEmp)

print("IN PLACE SORTING")
lstEmp.sort(key=attrgetter("name"))
print("Sorted List of Employees (Name)        : ", lstEmp)

lstEmp.sort(key=attrgetter("age"))
print("Sorted List of Employees (Age)         : ", lstEmp)

lstEmp.sort(key=attrgetter("salary"))
print("Sorted List of Employees (Salary)      : ", lstEmp)