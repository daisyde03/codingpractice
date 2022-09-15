def rec(s):
    if len(s) == 0:
        return s
    else:
        return rec(s[1:]) + s[0]


s = "hello"
print(rec(s))

def rev(n):
    str1 = ''
    for i in reversed(range(len(n))):
        str1 = str1 + n[i]
    if n == str1:
        return str1
    else:
        print("not palindrome")
    return
x = 'bab'
print("reverse daisy si ", rev(x))
