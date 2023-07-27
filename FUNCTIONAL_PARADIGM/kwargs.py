def f(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

f(a=1, b=2, c=4, name='Alex', speed='300km')

def combination(*args, **kwargs):
    print(args, kwargs)

combination(1, None, False, 'String', a=1, b='hi', c=[1, 2])

def builtin_print(*args, sep=' ', end='\n'):
    print(args, sep, end)

builtin_print(1, 2, 3, sep='*', end='\n')

a = [1, 2, 3, 'Hello']
print(*a)
