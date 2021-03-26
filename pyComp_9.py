s = "the quick brown fox jumps over the lazy dog"

result = {item: s.count(item) for item in s}
print(result)