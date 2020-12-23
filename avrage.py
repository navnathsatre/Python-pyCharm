user_name=input("Enter value for user name ")
A=int(input("enter value for MATH "))
B=int(input("enter value for PHY "))
C=int(input("enter value for CHE "))
total=A+B+C
avg=total/3
#avg =float(avg)
print(f"your name is {user_name} and mark for MATH:{A} mark for PHY:{B}mark for CHE:{C}")
print(f"total is {total} out of 300")
print("Average is {:.2f}".format(avg))