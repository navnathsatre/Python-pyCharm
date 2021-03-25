# Args

def SumOfNumbers(*args):
    print("Args: ", args)
    print("Type(args): ", type(args))
    result = 0
    for item in args:
        result += item
    print("Result: ", result)


SumOfNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)