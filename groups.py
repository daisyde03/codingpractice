#problem statement
#https://www.codechef.com/submit/GROUPS?tab=statement
for _ in range(int(input())):
    s = input()
    c = 0
    s1 = 0
    for i in range(len(s)):
        if s[i] == '1':
            c += 1
        else:
            if c > 0:
                s1 += 1
            c = 0
    if c > 0:
        s1 += 1
    print(s1)
