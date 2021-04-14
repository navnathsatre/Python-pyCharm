class Employee:
    def __init__(self, firstName, lastName, age, salray):
        self.fn = firstName
        self.ln = lastName
        self.age = age
        self.salary = salray
        self.email = self.fn + "." + self.ln + "@gmail.com"

    def printDetails(self):
        print("Employee Details")
        print("FirstName: {}, LastName: {}, Age: {}, Salary: {}, Email: {}".format(
            self.fn, self.ln, self.age, self.salary, self.email
        ))


# Inherited / Derived / Subclass / Child
class Developer(Employee):
    pass


class Manager(Employee):
    pass


e1 = Employee("Virat", "Kohli", 32, 5000)
e1.printDetails()

e2 = Developer("Ashwin", "R", 33, 6000)
e2.printDetails()

e3 = Manager("MS", "Dhoni", 39, 10000)
e3.printDetails()