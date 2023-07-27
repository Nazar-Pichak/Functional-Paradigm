import math

print(math.comb(5, 3))

def factorial(x):
    prog = 1
    for i in range(2, x + 1):
        prog = prog * i
    return prog

def binomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

bin = binomial(5, 3)
print(int(bin))

