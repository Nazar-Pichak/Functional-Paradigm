# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
# Closures help to invoke functions outside their scope.
# When and why to use Closures:
# 1. As closures are used as callback functions, they provide some sort of data hiding. This helps us to reduce the use of global variables.
# 2. When we have few functions in our code, closures prove to be an efficient way. But if we need to have many functions, then go for class (OOP). 


def main_func(value):
    name = value
    def inner_func():
        print('Hello my frined', name)

    return inner_func

call = main_func('Alex')
call()
print(call)

call_ = main_func('James')
call_()
print(call_.__closure__)

# adder

def adder(x):
    def inner(y):
        return x + y
    return inner

var = adder(5)
print(var(3))
