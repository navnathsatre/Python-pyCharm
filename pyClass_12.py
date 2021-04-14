from abc import ABC, abstractmethod

# abc is abstract base class

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def printName(self):
        print("I am in shape class")

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print("Square Area  : ", self.length * self.length)

class Rectange(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Rectange Area  : ", self.length * self.breadth)

    # def area(self, name):
    #     print("Name is: ", name)

# s1 = Shape()

sq1 = Square(5)
sq1.area()
sq1.printName()

r1 = Rectange(3, 5)
r1.area()
# r1.area("Welcome")
r1.printName()

print("--------------------")

lstObjects = [sq1, r1]
for item in lstObjects:
    item.area()
    item.printName()