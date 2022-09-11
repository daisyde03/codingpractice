#problem statement
#https://www.codechef.com/submit/ALTER
# cook your dish here
for _ in range(int(input())):
    l=list(map(int,input().split()))
    a=l[0]
    b=l[1]
    p=l[2]
    q=l[3]
    if(p%a!=0 or q%b!=0):
        print('NO')
    else:
        alice=(p//a)
        bob=(q//b)
        if(abs(alice-bob)<=1):
            print("YES")
        else:
            print("NO")