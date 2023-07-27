# In Python all variables are references to objects in the memory.

import ctypes
import sys

counter = 100               # Here integer object will have one reference
max = counter               # Here the same integer object will have two references and these references are the same. 

print(id(counter), id(max))

max = 999                   # If we assign a new value here, the number of references of the same 'integer' object
                            # will reduce by one.

counter = 10                # And if we assign a new value here, the number of references to the previos object reduce again by one and will equal zero.
                            # If an object does not have any references Python Memory Manager will destroy this object and reclaim the memory.

# To count the number of references we can use built-in module ctypes and his method from_address() or module sys and his method getrefcount

object_1 = [1, 2, 3]
object_2 = object_1
object_3 = None             # if we assign here None the number of references will reduce by one

print(object_1, object_2, object_3)

def count_ref(object_):
    return ctypes.c_long.from_address(object_).value

print(count_ref(id(object_1)))

s_ = {1: 2}
print(count_ref(id(s_)))

text = 'pppp'
print(count_ref(id(text))) 

print(sys.getrefcount(s_))
