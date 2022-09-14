#problem statement
#https://www.codechef.com/submit/PALL01
t =int(input())
for i in range(t):
    n =int(input())
    r = 0
    d =0
    temp = n
    while n != 0:
        d = n %10
        r = r*10+d
        n= n//10
    if r == temp:
        print("wins")
    else:
        print("loses")