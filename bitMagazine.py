#problem statement
#https://www.codechef.com/submit/TRMAG?

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    x=(n*(n+1))/2
    for i in range(1,l[0]+1):
        x=x-l[i]
    f=int(input())
    n = int((n + 1) / 2)
    x=x*(n-f)/n
    print("%.4f"%x)