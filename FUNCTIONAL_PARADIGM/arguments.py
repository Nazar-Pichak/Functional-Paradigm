def f(a, b, c):
    print(a, b, c)

#positional assigning
f(1, 2, 5)

#name assigning
f(b=23, c=12, a=3)

#combination
f(23, b=34, c='hi')

#default arguments
def func(a, b, c='default value'):
    print(a, b, c)

func(None, 'Hello')