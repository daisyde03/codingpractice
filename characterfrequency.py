s = str(input())
newstr = s[0]
str1 = ''
c = 1
for i in range(1, len(s)):

    if s[i] == newstr:
        c += 1
    else:
        str1 += str(newstr + str(c))
        newstr = s[i]
        c = 1

print(str1)

s = str(input())
# string1 = GeekksseekkGGggddgg
c = 1
for i in range(0, len(s)):
    str1 = s[i]
    c = 1
    for j in range(1, len(s)):
        temp = ''
        if s[j] == str1:
            c += 1
        else:
            temp += str(s[j] + str(c))
            # c = 1
            # print(str1)
