#problem statement
#https://www.codechef.com/submit/ALTARAY?tab=statement

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    li = [0]*n
    li[n-1] =1
    j = n-2
    while j >= 0:
        if (a[j] < 0 and a[j+1] > 0 or a[j] > 0 and a[j+1] < 0):
            li[j] = li[j+1] + 1
        else:
            li[j] = 1
        j -= 1
    for i in li:
        print(i,end = " ")
    print()
    
