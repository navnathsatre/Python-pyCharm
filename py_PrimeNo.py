# Write a program to find prime numbers between 100 and 200

# for item in range(100, 200):
#     100
#     whether it is divisble by any number between 2 and 99
#     for idiv in range(2, item)


for item in range(100, 200):
    isPrime = True
    for idiv in range(2, item):
        if item % idiv == 0:
            isPrime = False
            break

    if isPrime:
        print(item, end=",")