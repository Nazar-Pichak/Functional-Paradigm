# A closure is a function and an extended scope that contains free variables.
# Python cells and multi-scoped variables:
# The value of the greeting variable is shared between two scopes of:
# 1 The say function.
# 2 The closure
# The labels messages is in two different scopes.
# However, they always reference the same string objects with the value 'Hello' and 'World'.
# To achieve this, Python creates an intermediary object called a cell.
# To find the memory address of the cell object, you can use the __closure__ property as follows.

def say():
    message_1 = 'Hello'
    message_2 = 'World!'

    def display():
        print(f'{message_1} + {message_2}')

    return display

closure_var = say()
closure_var()
print()

print(say)
print(closure_var)
print()

print(type(say))
print(type(closure_var))
print()

print(closure_var.__closure__)
print(closure_var.__code__.co_freevars)