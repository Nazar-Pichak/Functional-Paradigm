*a, b, c = [None, True, False, 1, 2, 'Text...' ]
print(a, b, c)

e, *d, r = [1, 2, 3, None, False, 'String....']
print(e, d, r)

f, g, *h = (2, 3, 'Hello', [1, 2, 3])
print(f, g, h)

s = [1, 6]
print(list(range(*s)))

