# Sorting on dictionaries
d = {"A": 1, "D": 4, "B": 2, "C": 3}

print("Original dict  : ", d)
s_d = sorted(d)
s_d_values = sorted(d.values())

print("Sorted function on d (keys)  : ", s_d)
print("Sorted function on d (values): ", s_d_values)