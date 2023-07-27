# closure

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

count_var = counter()
print(count_var())
print(count_var())
print(count_var())
print(count_var())
print(count_var())
print(count_var())
