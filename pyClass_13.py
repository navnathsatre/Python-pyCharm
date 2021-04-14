class Student:
    def __init__(self, name):
        self.name = name

    # def __del__(self):
    #     print("I am in __del__")


s1 = Student("Virat")
s2 = Student("Dhoni")

s2.age = 37

print("s1 dict          : ", s1.__dict__)
print("s2 dict          : ", s2.__dict__)

# Monkey Patching
