# Sorting based on keys param
usrList = [-9, 1, 8, 2, -7, 3, 6, -4, 5, 4]
print("Original List : ", usrList)

s_li = sorted(usrList, key=abs) # NON-INPLACE SORTING
#s_li = sorted(usrList)
print("Sorted List   : ", s_li)
print("Original List : ", usrList)

# print("Sorting using inbulit method")
# usrList.sort() # IN- PLACE SORTING
# print("Original List : ", usrList)