#problem statement
#https://www.codechef.com/submit/FILL01?

for i in range(int(input())):
    n, k = map(int, input().split())
    s = str(input())
    c = 0
    x = s.split('1')
    for j in range(len(x)):
        if len(x[j]) < k:
            pass
        else:
            c += (len(x[j]) // k)
    print(c)


