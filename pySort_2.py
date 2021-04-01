usrList = [9, 1, 8, 2, 7, 3, 6, 4, 5]


print("Original List : ", usrList)

s_li = sorted(usrList, reverse=True) # NON-INPLACE SORTING

print("Sorted List   : ", s_li)
print("Original List : ", usrList)

print("Sorting using inbulit method")
usrList.sort(reverse=True) # IN- PLACE SORTING
print("Original List : ", usrList)
