# Fibonacci series   (addition of previous two)
# Fib(0) = 0
# Fib(1) = 1
# Fib(2) = Fib(1) + Fib(0) == 1 + 0 == 1
# Fib(3) = Fib(2) + Fib(1) == 1 + 1 == 2
# Fib(n) = Fib(n-1) + Fib(n-2)

# Fib(5)
# 0 1 1 2 3 5

# Write a program to print Fibonacci Series
lookup = {}
# lookup = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, ...}
def fibo(n):
    if n == 0 or n == 1:
        lookup[n] = n

    if n not in lookup:
        lookup[n] = fibo(n-1) + fibo(n-2)

    return lookup[n]

num = int(input("Enter any number: "))
for item in range(num + 1):
    print(fibo(item), end=" ")

a, b = 0, 1
for item in range(41):
    print(a, end=" ")
    a, b = b, a + b