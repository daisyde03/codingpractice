#problem statement
#https://www.codechef.com/submit/VOLCONTROL

# cook your dish here
t= int(input())
for t in range(t):
    a,b =map(int,input().split())
    if a>b:
        vol=a-b
    else:
        vol=b-a
    print(vol)

    T = int(input())
    a = [100, 50, 10, 5, 2, 1]
    for _ in range(T):
        n = int(input())
        b = 0
        for x in a:
            if (x <= n):
                b = b + (n // x)
                n = n % x
        print(b)