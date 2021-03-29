# nums = list(range(1, 11))
# nums = range(1, 11)
nums = tuple(range(1, 11))
print("Numbers : ", nums)

even = lambda num: num % 2 == 0

print(even(5))
print(even(10))

result = filter(even, nums)
print("Result using filter - even: ", result)
print("Type of result: ", type(result))
print("List from result using filter - even: ", tuple(result))
print("List from result using filter - even: ", list(result))

# ===============================================

result = map(even, nums)
print("Result using map - even: ", result)
print("Type of result: ", type(result))
print("List from result using map - even: ", list(result))