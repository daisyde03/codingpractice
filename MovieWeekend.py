#problem statement
#https://www.codechef.com/submit/MOVIEWKNs

for i in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [a[i]*b[i] for i in range(n)]
    m = max(c)
    d=-100
    x =0
    for i in range(n):
        if c[i]<m:
            continue

        if b[i]-a[i]>d:
            d = b[i]-a[i]
            x=i

    print(x+1)
