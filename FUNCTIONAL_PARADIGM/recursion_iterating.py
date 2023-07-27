even = []

def list_(a, b=0):
    global even

    if len(a) != b:
        if a[b] % 2 == 0:
            even.append(a[b])
            print(even)
        list_(a, b + 1)

a = range(10 + 1)
list_(a)


digits = ''

def str_(s, i=0):
    global digits 

    if len(s) != i:
        if s[i].isdigit():
            digits += s[i]
            print(digits)
        str_(s, i + 1)

s = 'some text here...and digits 1 2 3 4  5 6 7'
str_(s)

def dic_(d, i=0):
    if len(d) != i:
        print(d.values())
        dic_(d, i + 1)

diction = {'digits': digits, 'even': even }
dic_(diction)