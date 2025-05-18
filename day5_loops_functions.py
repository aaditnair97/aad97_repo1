def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

x = int(input("Enter the number to find the factorial:"))
print(factorial(x))