# closure Part 2

def average_number():
    sume = 0
    quantity = 0
    def inner(number):
        nonlocal sume
        nonlocal quantity
        sume = sume + number
        quantity += 1
        return sume / quantity
    return inner
    
a = average_number()

print(a(10))
print(a(4))
print(a(10))
print(a(5))
print(a(7))
print(a(12))
