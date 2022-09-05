#problem statement
#https://www.codechef.com/submit/BOUQUET

t = int(input())
for i in range(t):
    m = list(map(int, input().split()))
    o = list(map(int, input().split()))
    p = list(map(int, input().split()))
    m = max([sum(m), sum(o), sum(p)] + [sum(x) for x in zip(m,o,p)])
    if m > 0:
        if m % 2 ==0:
            print(m-1)
        else:
            print(m)
    else:
        print(0)
