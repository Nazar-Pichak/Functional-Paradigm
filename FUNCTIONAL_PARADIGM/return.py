def square1(x):
    print(x ** 2)
    return None

a = square1(6)
print(a)

def square2(x):
    return x ** 2

b = square2(5)
print(b)

def even_numbers(x):
    return x % 2 == 0

for i in range(1, 11):
    print(i, even_numbers(i))
    