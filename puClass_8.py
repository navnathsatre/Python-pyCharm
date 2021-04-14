class Employee:
    __employee_count = 0
    __employee_left = 0

    def __init__(self, firstName, lastName, age, salray):
        self.fn = firstName
        self.ln = lastName
        self.age = age
        self.salary = salray
        self.email = self.fn + "." + self.ln + "@gmail.com"
        Employee.__employee_count += 1

    # Decorator
    @classmethod
    def GetEmployeeCount(cls):
        return cls.__employee_count

    def printDetails(self):
        print("Employee Details")
        print("FirstName: {}, LastName: {}, Age: {}, Salary: {}, Email: {}".format(
            self.fn, self.ln, self.age, self.salary, self.email
        ))


e1 = Employee("Virat", "Kohli", 32, 5000)
e1.printDetails()
print("Employee dict: ", Employee.__dict__)
print("e1 dict : ", e1.__dict__)

e2 = Employee("MS", "Dhoni", 35, 7000)
print("Employee dict after MSD: ", Employee.__dict__)

# print("Employee count using e1 (instance/object) : ", e1.__employee_count) # Error
# print("Employee count using class: ", Employee.__employee_count) # error

print("Employee count using class method: ", Employee.GetEmployeeCount())
print("Employee count using class method at instance level: ", e1.GetEmployeeCount())