#problemStatement
#https://www.codechef.com/submit/MANIPULATE

t = int(input())
while t > 0:
    a, b = map(int, input().split())
    if a >= b:
        print("YES")
    else:
        print("NO")
    t -= 1

