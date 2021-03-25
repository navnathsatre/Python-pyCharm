def multipleUnpackings(*args):
    print("Args: ", args)
    print("Type of Args: ", type(args))


a = [1, 2, 3]
multipleUnpackings(*a)

b = (4, 5, 6)
multipleUnpackings(*b)

c = {4, 5, 6}
multipleUnpackings(*c)

r = range(100, 105)
multipleUnpackings(*r)

print(*range(1, 6), sep='')
#print(*range(1, 6), sep="\n")

# PYTHON 3.5 ==> This feature is available ONLY from Python 3.5
