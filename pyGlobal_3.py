runscored = 1

def localFunction():
    runscored = 2 ## creates a new local object
    print("The value of runscored in localFunction() : ", runscored)


def globalFunction():
    global runscored
    runscored = 3
    print("The value of runscored in globalFunction(): ", runscored)


print("The value of runscored in main: ", runscored)
localFunction()
print("After calling localFunction, the value of runscored in main: ", runscored)

globalFunction()
print("After calling globalFunction, the value of runscored in main: ", runscored)

localFunction()
print("After calling localFunction, the value of runscored in main: ", runscored)


