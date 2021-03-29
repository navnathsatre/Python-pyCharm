def myFunction():
    global temp
    temp = "Global Variable"
    print("Value of temp INSIDE myFunction: ", temp)


myFunction()
print("Value of temp OUTSIDE myFunction: ", temp)