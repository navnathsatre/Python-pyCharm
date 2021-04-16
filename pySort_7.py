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


def sortKeyEmployeeName(emp):
    return emp.name

def sortKeyEmployeeAge(emp):
    return emp.age

def sortKeyEmployeeSalary(emp):
    return emp.salary

sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeName)
print("Sorted list of Employees (name)              : ", sortedLstEmp)

sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeAge)
print("Sorted list of Employees (age)               : ", sortedLstEmp)

sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeSalary)
print("Sorted list of Employees (salary)            : ", sortedLstEmp)

print("Reverse Sorting")
sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeName, reverse=True)
print("Sorted list of Employees (name)              : ", sortedLstEmp)

sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeAge, reverse=True)
print("Sorted list of Employees (age)               : ", sortedLstEmp)

sortedLstEmp = sorted(lstEmp, key=sortKeyEmployeeSalary, reverse=True)
print("Sorted list of Employees (salary)            : ", sortedLstEmp)

print("IN PLACE SORTING")
lstEmp.sort(key=sortKeyEmployeeName)
print("Sorted List of Employees (Name)        : ", lstEmp)

lstEmp.sort(key=sortKeyEmployeeAge)
print("Sorted List of Employees (Age)         : ", lstEmp)

lstEmp.sort(key=sortKeyEmployeeSalary)
print("Sorted List of Employees (Salary)      : ", lstEmp)

print("----------------------------------------")
print("IN PLACE LAMBDA SORTING")
lstEmp.sort(key=lambda emp: emp.name)
print("Sorted List of Employees (Name)        : ", lstEmp)

lstEmp.sort(key=lambda emp: emp.age)
print("Sorted List of Employees (Age)         : ", lstEmp)

lstEmp.sort(key=lambda emp: emp.salary)
print("Sorted List of Employees (Salary)      : ", lstEmp)