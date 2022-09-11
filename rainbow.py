#problem Statement
#https://www.codechef.com/submit/RAINBOWA?

def distinct(a):
    b=[]
    for i in a:
        if a not in b:
            b.append(i)
    return b
k=[1,2,3,4,5,6,7]
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if a==a[::-1] and set(distinct(a))==set(k) and sorted(a[:n//2])==a[:n//2] :
        print('yes')
    else:
        print('no')