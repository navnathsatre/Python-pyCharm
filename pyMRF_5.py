from functools import reduce

nums = list(range(1, 11))
print("Numbers: ", nums)

addNo = lambda x, y: x + y
print(addNo(100, 200))

result = reduce(addNo, nums)
print("Result: ", result)


multiply = lambda x, y: x * y

result = reduce(multiply, nums)
print("Result: ", result)


#