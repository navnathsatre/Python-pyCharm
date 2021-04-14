class Employee:
    def __init__(self, firstName, lastName, age, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.salary = salary
        self.email = firstName + "." + lastName + "@gmail.com"

    def printDetails(self):
        print("First Name: {}, Last Name: {}, Age: {}, Salary: {}, Email: {}".format(
            self.firstName, self.lastName, self.age, self.salary, self.email
        ))

    @classmethod
    def fromString(cls, empStr):
        first, last, age, salary = empStr.split("-")
        return cls(first, last, age, salary)

    @staticmethod
    def isWorkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


e1 = Employee("Virat", "Kohli", 32, 5000)
e1.printDetails()
print("------------------------------")
e2_user_str = "Gautam-Gambhir-33-6000"
e4 = Employee.fromString(e2_user_str)
e4.printDetails()


import datetime

today = datetime.date(2017, 6, 10)
print(e1.isWorkday(today))
print(Employee.isWorkday(today))