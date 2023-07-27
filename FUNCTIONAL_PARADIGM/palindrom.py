def palindrom(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    return palindrom(s[1: -1])

string = input()
print(palindrom(string))