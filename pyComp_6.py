s = "Welcome to the word of python programming"

#split
lstWords = s.split(" ")
print(lstWords)

# Write a program to generate below output
# [("Welcome", 7), ("to", 2), ("the", 3), ...]

result = []
for item in lstWords:
    result.append((item, len(item)))

print(result)

# Using LC
result = [(item, len(item)) for item in lstWords]
print(result)