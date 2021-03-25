EmptyListAsParam(my_list=[]):
    my_list.append("$")
    return my_list


r = EmptyListAsParam()
print("Returned Output 1st Iteration: ", r)

r1 = EmptyListAsParam()
print("Returned Output 2nd Iteration: ", r1)

r2 = EmptyListAsParam()
print("Returned Output 2nd Iteration: ", r2)

r3 = EmptyListAsParam([1, 2, 3])
print("Returned Output 2nd Iteration: ", r3)

r4 = EmptyListAsParam([1, 2, 3])
print("Returned Output 2nd Iteration: ", r4)