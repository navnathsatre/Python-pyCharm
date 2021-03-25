def namedArgumentFunction(a, b, c):
    print("The values are a: {}, b: {}, c: {}".format(a, b, c))


namedArgumentFunction(100, 200, 300) # Positional arguments
namedArgumentFunction(c=3, a=1, b=2) # Named arguments
#namedArgumentFunction(101, a=102, c=103) # Mix of Postion + Name # error
#namedArgumentFunction(b=600, 500, c=103) # Positional argument after named argument, error
namedArgumentFunction(101, b=102, c=103) # Mix of Postion + Name
#namedArgumentFunction(a=600, 500, c=900) # Positional argument after named argument, error