# Lambda Function
# Anonymous function
# function which have got NO names
# They are used to write one-line function

def mySquare (num):
    return num * num

print(mySquare(7))


f = lambda num: num * num
print(f)
print(type(f))
result = f(5)
print("Square of number: ",result)

print("Square of number: ", (lambda num: num * num)(10)) # we can use user input also



f = lambda x, y: x if x > y else y
print("Max of 3, 5 : ",f(3, 5))