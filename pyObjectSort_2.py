from operator import attrgetter

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


s_li_emp_name = sorted(lstEmp, key=attrgetter("name"))
print("Sorted list of employees (NAME)              : ", s_li_emp_name)

s_li_emp_age = sorted(lstEmp, key=attrgetter("age"))
print("Sorted list of employees (AGE)               : ", s_li_emp_age)

s_li_emp_salary = sorted(lstEmp, key=attrgetter("salary"))
print("Sorted list of employees (SALARY)            : ", s_li_emp_salary)