#all(iterable, /)
#    Return True if bool(x) is True for all values x in the iterable.
#    
#    If the iterable is empty, return True.

a = ['apple', 1, 2, [1, -3, 9], ('Hello', 'Hi', 'How are you')]
print(all(a))
b = ['', 1, 2, 'some text', ('tuple', 'and')]
print(all(b))
print(all(''))
print()

#any(iterable, /)
#    Return True if bool(x) is True for any x in the iterable.
#    
#    If the iterable is empty, return False.

c = 0, '', [], (), {}, 'String'
print(any(c))
d = [0, '', [], (), {}]
print(any(d))
print(any(''))
print()

collection = [1, 2.3, 'string', ['list', 1, 3], ('tuple', 1), {'set', 3}, \
    {'d_key': 'value'}, 0, 0.0, '', [], (), {}]

map_object = list(map(bool, collection))
print(map_object)
