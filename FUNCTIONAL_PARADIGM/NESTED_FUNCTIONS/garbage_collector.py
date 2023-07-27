# In C/C++, you’re fully responsible for managing the memory of the program.
# However, in Python, you don’t have to manage the memory yourself because Python does it for you automatically.
# Here is presented how garbage collector works and how we can controll counting references.
# And something about circular references. 

import gc
import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_exists(object_id):
    for object in gc.get_objects():
        if id(object) == object_id:
            return True

    return False


class A:
    def __init__(self):
        self.b = B(self)
        print(f'A: {hex(id(self))}, B: {hex(id(self.b))}')


class B:
    def __init__(self, a):
        self.a = a
        print(f'B: {hex(id(self))}, A: {hex(id(self.a))}')

gc.disable()

a = A()

a_id = id(a)
b_id = id(a.b)

print(ref_count(a_id))  # 2
print(ref_count(b_id))  # 1

print(object_exists(a_id))  # True
print(object_exists(b_id))  # True

a = None
print(ref_count(a_id))  # 1
print(ref_count(b_id))  # 1

print(object_exists(a_id))  # True
print(object_exists(b_id))  # True

# By enabling the garbage collector it is detecting the circular references and destrying these objects.
gc.collect()

print(object_exists(a_id))  # True
print(object_exists(b_id))  # True