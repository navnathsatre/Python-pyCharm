class Student:
    def __init__(self, name):
        self.name = name
        self.grades = 0
        self.times = 0

    def addGrade(self, marks):
        self.grades += marks
        self.times += 1

    def getAverage(self):
        if self.times > 0:
            return self.grades / self.times
        else:
            return "empty grades"

s1 = Student("Virat")
s2 = Student("MS Dhoni")

print("s1 dict      : ", s1.__dict__)
s1.addGrade(10)
s1.addGrade(20)
s1.addGrade(30)
print("s1 dict after adding grades     : ", s1.__dict__)
print("s2 dict after adding grades     : ", s2.__dict__)

print("S1 Average: ", s1.getAverage())
print("S2 Average: ", s2.getAverage())
