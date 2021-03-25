# Positional + keyword - Only Arguments (Available ONLY from Python 3.8)

def positionalkeywordArguments(a, b, /, z, w, *, x, y):
    print("a: {}, b: {}, z: {}, w: {}, x: {}, y: {}".format(a, b, z, w, x, y))


# positionalkeywordArguments(1, 2, 3, 4, 5, 6) # error as x, y needs to passed via keyword arguments
positionalkeywordArguments(1, 2, 3, 4, x=5, y=6)
positionalkeywordArguments(1, 2, z=3, w=4, x=5, y=6)
