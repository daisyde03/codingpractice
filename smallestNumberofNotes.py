
#problem statement
#https://www.codechef.com/submit/FLOW005

t = int(input())
a =[100,50,20,5,2,1]
for i in range(t):
    n = int(input())
    b= 0
    for x in a:
        if x <= n:
            b = b + (n // x)
            n= n % x
    print (b)