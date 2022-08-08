#Problem statement:
#https://www.codechef.com/submit/CANDY123?tab=statement

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    n = 1000
    for i in range(n):
        if (i % 2 == 1):
            a = a - i
            if a < 0:
                print("Bob")
                break
        else:
            b = b - i
            if b < 0:
                print("Limak")
                break
