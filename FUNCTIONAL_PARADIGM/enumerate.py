# Builtin function ENUMERATE

a = [10, 20, 30, 40, 50, 60, 70]

print(list(enumerate(a)))

for index, value in enumerate(a, start=1):
    print(index, value)

for index, value in enumerate(a):
    a[index] += 1

print(a)

for index, value in enumerate(range(10, 21)):
    print(index, value)

