#problem statement
#https://www.codechef.com/submit/CHEFWORK?tab=statement

n=int(input())
coins=list(map(int,input().split()))
workers=list(map(int,input().split()))
a=9999
b=9999
c=9999
for i in range (n):
    if(workers[i]==1):
        a=min(a,coins[i])
    elif(workers[i]==2):
        b=min(b,coins[i])
    else:
        c=min(c,coins[i])
if(c>a+b):
    print(a+b)
else:
    print(c)