from operator import itemgetter
lstEmp = [("ABC", 25, 700), ("DEF", 65, 70), ("XYZ", 55, 7000)]

print("Original List of Employees       : ", lstEmp)

s_lstEmp = sorted(lstEmp, key=itemgetter(0))
print("Sorted List of Employees (name)      : ", s_lstEmp)

s_lstEmp = sorted(lstEmp, key=itemgetter(1))
print("Sorted List of Employees (age )      : ", s_lstEmp)

s_lstEmp = sorted(lstEmp, key=itemgetter(2))
print("Sorted List of Employees (salary)    : ", s_lstEmp)