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
    def __init__(self, firstName, lastName, age, salary, proglang):
        super().__init__(firstName, lastName, age, salary)
        # Employee.__init__()
        self.proglang = proglang

    def printDetails(self):
        super().printDetails()
        print("Programming Language: ", self.proglang)


class Manager(Employee):
    def __init__(self, firstName, lastName, age, salary, lstEmployees=None):
        super().__init__(firstName, lastName, age, salary)
        if lstEmployees is None:
            self.lstEmployees = []
        else:
            self.lstEmployees = lstEmployees

    def addEmployee(self, emp):
        if emp not in self.lstEmployees:
            self.lstEmployees.append(emp)

    def removeEmployee(self, emp):
        if emp in self.lstEmployees:
            self.lstEmployees.remove(emp)

    def printDetails(self):
        super().printDetails()
        print("Employees reporting to Manager:")
        for item in self.lstEmployees:
            print("--->", item.fn + "--" + item.ln)


e1 = Employee("Virat", "Kohli", 32, 5000)
e2 = Developer("R", "Ashwin", 33, 6000, "Python")
e3 = Manager("MS", "Dhoni", 34, 7000, [e1, e2])

e1.printDetails()
print("--------------------------------")
e2.printDetails()
print("--------------------------------")
e3.printDetails()
print("--------------------------------")

print("Is e3 instance of Manager        : ", isinstance(e3, Manager))
print("Is e2 instance of Manager        : ", isinstance(e2, Manager))

print("Is Developer subclass of Employee    : ", issubclass(Developer, Employee))
print("Is Manager   subclass of Employee    : ", issubclass(Manager, Employee))
print("Is Developer   subclass of Manager   : ", issubclass(Developer, Manager))