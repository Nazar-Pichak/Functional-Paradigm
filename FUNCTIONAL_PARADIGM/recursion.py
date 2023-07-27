def recursion(x):
    if x < 4:
        print(x)
        recursion(x + 1)
        print(x)

recursion(1)