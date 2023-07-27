def factorial(n):
    if n == 1:
        return 1
    return factorial(n -1) * n

for i in range(1, 11):
    print(i, factorial(i))