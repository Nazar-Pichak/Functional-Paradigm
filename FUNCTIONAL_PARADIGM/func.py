def greeting():
    print("Hello")
    print('World!!!')
    print('I am function')

greeting()
print('pause')
greeting()
print()

def square_number(x):
    print('The square of number', x, '=', x**2)
    
for i in range(1, 11):
    square_number(i)

def multiply(x, y):
    print('Result =', x * y)

for i in range(1, 11):
    multiply(i, i)


def even_number(x):
    if x % 2 == 0:
        print(x, 'is even number')
    else:
        print(x, 'is odd number')

for i in range(10, 31):
    even_number(i)

def factorial(n):
    progression = 1
    for i in range(2, n + 1):
        progression = progression * i
    print(progression)

factorial(4)