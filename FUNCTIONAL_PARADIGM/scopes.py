len = 'global scope and namespace'

def f():
    len = 'enclosing scope and namespace'
    print(len)

    def a():
        len = 'local scope and namespace'
        print(len)
    a()    
f()
print(len)

def a():
    def b():
        print(sum, 'builtin scope and name space')
    b()
a()

