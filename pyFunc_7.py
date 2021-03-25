# Function as a PARAMETER

def mySquare(num):
    return num + num

# mySquare(10)

#def myCube(n):
 #   return n * n * n

def WrapperFuncton(FuncAsParam, num):
    print("Type of FuncAsParam: ", type(FuncAsParam))
    return FuncAsParam(num)


result = WrapperFuncton(mySquare, 5)
print("Result: ", result)

# Functions are also first class object in python
#Closures
#Decorators