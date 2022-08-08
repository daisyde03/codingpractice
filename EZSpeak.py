#problem statement
#https://www.codechef.com/submit/EZSPEAK

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    c = 0
    for j in range(n):
        if (s[j]=="a" or s[j]=="e" or s[j]=="i" or s[j]=="o" or s[j]=="u"):
            c = 0
        else:
            c += 1
        if c >= 4:
            break
    if c >= 4:
        print("NO")
    else:
        print("YES")