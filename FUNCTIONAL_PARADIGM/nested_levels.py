# Control levels of nesting with recursions help.

a = [1, 2, [10, 20, [30, 40, [50, 60, 70]]], [4, 5, [10, 29, 30, [-1, -2, -4, -5]]]]

def recursion(list_, level=1):
    print(*list_, 'level = ', level)

    for i in list_:
        if type(i) == list:
            recursion(i, level + 1)


recursion(a)