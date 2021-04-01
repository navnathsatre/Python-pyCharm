usrTuple = (9, 1, 8, 2, 7, 3, 6, 4, 5)


print("Original Tuple : ", usrTuple)

s_li = sorted(usrTuple, reverse=True) # NON-INPLACE SORTING

print("Sorted List   : ", s_li)
print("Sorted Tuple  : ", tuple(s_li))
print("Original Tuple : ", usrTuple)

# There is no IN-PLACE sorting for tuple (as tuples are IMMUTABLE)