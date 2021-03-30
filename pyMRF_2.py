nums = list(range(1, 11))
print("Numbers : ", nums)

sq = lambda num: num * num

# mobject = map(sq, nums)
mobject = map(sq, range(1, 11))
print(mobject)
print(type(mobject))

print("List of Square of nums using Map: ", list(mobject))
print("Tuple of Square of nums using Map: ", tuple(mobject))