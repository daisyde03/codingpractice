#problem statement
#https://www.codechef.com/submit/COMPRESSVD
t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().strip().split()))
    str1 = str(s)
    count =1
    for j in range(1,n):
        if s[j-1] != s[j]:
            count += 1
    print(count)
    