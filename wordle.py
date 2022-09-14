#problem statement
#https://www.codechef.com/submit/WORDLE

t = int(input())
M = ''
for i in range(t):
    s = str(input())
    t = str(input())
    for j in range(len(s)):
        if s[j] == t[j]:
            M = str(M + "G")

        else:
            M = str(M + "B")
    print(M)