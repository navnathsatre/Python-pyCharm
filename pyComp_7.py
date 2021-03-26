s = "Welcome to the word of python programming. the word is full of programmer"

#split
lstWords = s.split(" ")
print(lstWords)

# Write a program to generate below output
# [("Welcome", 7), ("to", 2), ("the", 3), ...]

result = []
for index, item in enumerate(lstWords):
    result.append(index, item, len(item))

print(result)



s = "Welcome to the world of Python Programming. the world is full of programmers"

# [(0, "Welcome", 7), (1, "to", 2), (2, "the", 3) ...]

lstWords = s.split(" ")

# enumerate
result = [(index, item, len(item)) for index, item in enumerate(lstWords)]
print(result)