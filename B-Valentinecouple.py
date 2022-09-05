#problem statement
#https://www.codechef.com/submit/VCOUPLE

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    a.sort()
    b.sort(reverse = True)
    max =0
    for j in range(n):
        temp = a[j] + b[j]
        if temp > max:
            max = temp
    print(max)