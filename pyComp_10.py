alphabets = ['a', 'b', 'c', 'd']
fruits = ['apple', 'banana', 'cherry', 'dates']

# using the above two lists, create a dictionary using dictionary comprehension
# {'a': "apple", 'b': "banana", ...}

# result = {alphabets[item]: fruits[item] for item in range(0, 4)}
result = {alphabets[item]: fruits[item] for item in range(0, len(alphabets))}
print(result)