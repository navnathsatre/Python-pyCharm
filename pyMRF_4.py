# Take a sequence of numbers from the user
# 1st Number: Count
# 2nd ... Count: all are numbers

# 5 1 2 3 4 5
# 5 10 45 76 3 4
# 3 100 45 60

usrInput = input("")
print(usrInput)

lstNos = list(map(int, usrInput.split()))

print("List of Numbers: ", lstNos)


avg = sum(lstNos[1:]) / lstNos[0]
# avg = sum(lstNos[1:]) / len(lstNos[1:])
print(avg)