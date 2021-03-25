# Positional - Only Arguments (Available ONLY from Python 3.8)

def positionalArguments(a, b, /, z, x, y):
    print("a: {}, b: {}, z: {}, x: {}, y: {}".format(a, b, z, x, y))


positionalArguments(1, 2, 3, 4, 5)
positionalArguments(1, 2, z=3, y=5, x=4)
# positionalArguments(a=1, b=2, z=3)
