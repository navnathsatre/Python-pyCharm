# Dictionary Comprehension
# {1: 1, 2: 4, 3: 9, 4: 16,..}
result = {item: item * item for item in range(1, 11)}
print(result)

result = {}
for item in range(1, 11):
    result[item] = item * item

print(result)