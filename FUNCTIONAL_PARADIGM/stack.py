def f1(arg):
    return f2(arg)

def f2(arg):
    return f3(arg)

def f3(arg):
    return 1 / arg

print(f1(10))

