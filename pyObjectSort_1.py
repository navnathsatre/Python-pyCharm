class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return "{}-{}-{}".format(self.name, self.age, self.salary)


e1 = Employee("ABC", 25, 700)
e2 = Employee("DEF", 85, 7000)
e3 = Employee("XYZ", 65, 70)

lstEmp = [e1, e2, e3]
print("List of employees                            : ", lstEmp)


def sortBasedOnName(emp):
    return emp.name

def sortBasedOnAge(emp):
    return emp.age

def sortBasedOnSalary(emp):
    return emp.salary

s_li_emp_name = sorted(lstEmp, key=sortBasedOnName)
print("Sorted list of employees (NAME)              : ", s_li_emp_name)

s_li_emp_age = sorted(lstEmp, key=sortBasedOnAge)
print("Sorted list of employees (AGE)               : ", s_li_emp_age)

s_li_emp_sal = sorted(lstEmp, key=sortBasedOnSalary)
print("Sorted list of employees (AGE)               : ", s_li_emp_sal)

print("REVERSE SORTING")
s_li_emp_name = sorted(lstEmp, key=sortBasedOnName, reverse=True)
print("Sorted list of employees (NAME)              : ", s_li_emp_name)

s_li_emp_age = sorted(lstEmp, key=sortBasedOnAge, reverse=True)
print("Sorted list of employees (AGE)               : ", s_li_emp_age)

s_li_emp_sal = sorted(lstEmp, key=sortBasedOnSalary, reverse=True)
print("Sorted list of employees (AGE)               : ", s_li_emp_sal)


# if e1 > e2:
#     print("e1 is greater than e2")
#
# x = 10
# y = 20
#
# if x > y:
#     print("x is greater than y")
#
# int()