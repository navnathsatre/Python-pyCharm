def myFunction():
    a = "LocalValue"
    print(a)
    print("Inside myFunction")


myFunction()
# print(a)  ## Error, the scope of a is within myFunction
