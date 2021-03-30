s = "Welcome to the world of Python Programming. the world is full of programmers"

# [(0, "Welcome", 7), (1, "to", 2), (2, "the", 3) ...]

lstWords = s.split(" ")

# enumerate
result = [(index, item, len(item)) for index, item in enumerate(lstWords)]
print(result)