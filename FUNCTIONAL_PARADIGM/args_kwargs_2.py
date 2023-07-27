def func(a, b, c, d):
    print(a, b, c, d)

func(1, 2, 'Hello', None)

a = ('String...', None, False, 1)
func(*a)

def arguments(*args):
    print(args, type(args))

arguments(1, 2, None, False, ['apple', 'banan'])
arguments(3, None, 3)
arguments(1)
arguments()

def f(*args):
    sume = 0
    for i in args:
        sume += i
    return sume

print(f(1, 2, 3, 4, 5, 6, 7, 8, 9))
