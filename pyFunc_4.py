# Factorial of number
# 5! = 5 * 4!
# 4! = 4 * 3!

# n! = n * (n-1)!

def recurFactorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * recurFactorial(num-1)

n = int(input("Enter the number "))
out = recurFactorial(n)
print("Factorial of {} is {} ".format(n, out))