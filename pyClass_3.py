class Employee:
    '''
    Help: An Employee class documentation
    The instance of class can be used to create and manage Employee data
    It stores info like, name, address, education details etc
    '''
    def __init__(self, firstName, lastName):
        # Similar to constructor
        print("Value of self: ", self)
        self.fn = firstName
        self.ln = lastName


e1 = Employee("Virat", "Kohli")
e2 = Employee("MS", "Dhoni")

print("e1 : ", e1)
print("e2 : ", e2)

print("e1 dict              : ", e1.__dict__)
print("e2 dict              : ", e2.__dict__)
print("Employee dict        : ", Employee.__dict__)