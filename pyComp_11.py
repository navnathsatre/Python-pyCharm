alphabets = ["a", "b", "c", "d"]
fruits = ["apple", "banana", "cherry", "dates"]

# {"a": ("apple", 5), "b": ("banana", 6),... }

result = {alphabets[item]: (fruits[item], len(fruits[item])) for item in range(0, len(alphabets))}
print(result)