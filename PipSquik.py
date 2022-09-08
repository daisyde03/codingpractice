#problem statement
#https://www.codechef.com/submit/PIPSQUIK?tab=statement

# cook your dish here
t = int(input())
for i in range(t):
    n,h,y1,y2,l = map(int, input().split())
    c=0
    duck = h - y1
    jump = y2
    for j in range(n):
        t, x = map(int, input().split())
        if l > 0:
            if t == 1:
                if x < duck:
                    l -= 1
            elif t ==2:
                if x > jump:
                    l -= 1
        if l > 0:
            c += 1
    print(c)