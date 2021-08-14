from operator import itemgetter
lstEmp = [("ABC", 25, 700), ("DEF", 85, 7000), ("XYZ", 65, 70)]

print("Original list of employees:  ", lstEmp)

s_lst_emp = sorted(lstEmp, key=itemgetter(0))
print("Sorted list of employees (NAME)   : ", s_lst_emp)

s_li_emp_age = sorted(lstEmp, key=itemgetter(1))
print("Sorted list of employees (AGE)    : ", s_li_emp_age)

s_li_emp_salary = sorted(lstEmp, key=itemgetter(2))
print("Sorted list of employees (SALARY) : ", s_li_emp_salary)