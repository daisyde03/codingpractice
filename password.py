#problem statement
#https://www.codechef.com/submit/PASSWD

import re
for x in range(int(input())):
    s = str(input())
    length = len(s)
    num ='1234567890'
    special ='!@#$&?'
    caps = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    newstr = ''
    for i in range(1, length-1):
        newstr = newstr+s[i]
    n = re.findall("[0-9]" ,newstr)
    c = re.findall("[A-Z]", newstr)
    sp = re.findall("[!@#$&?]", newstr)
    sm = re.findall("[a-z]" ,s)
    if n and c and sp and sm and len(s) >= 10:
        print("yes")
    else:
        print("no")

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alphabetb = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# numbers = '1234567890'
# special = '@#%&?'
# for _ in range(int(input())):
#     password = input()
#     case1 = case2 = case3 = case4 = 0
#     case5 = (len(password) >= 10)
#     for a in alphabet:
#         if a in password:
#             case1 = 1
#             break
#     password = password[1:-1]
#     for ab in alphabetb:
#         if ab in password:
#             case2 = 1
#             break
#     for n in numbers:
#         if n in password:
#             case3 = 1
#             break
#     for s in special:
#         if s in password:
#             case4 = 1
#             break
#     if case1 and case2 and case3 and case4 and case5:
#         print('YES')
#     else:
#         print('NO')


