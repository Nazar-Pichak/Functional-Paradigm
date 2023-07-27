# Anonymous function LAMBDA

a = lambda a, b: a * b
print(a(10, 20))

triangle_perimeter = lambda a, b, c: a + b + c
print(triangle_perimeter(10, 10, 20))

list = [1, 2, 33, 2345, 234, 567, 23, 104, 50000]
list.sort(key=lambda x: x // 10 % 10)
print(list)

def linear(k, b):
    return lambda x: x * k + b

graf = linear(2, 5)
print(graf(3))
