#problem statement
#https://www.codechef.com/submit/NODRUGS?
# cook your dish here
t = int(input())
for i in range(t):
    n, k, l = map(int, input().split())
    a = list(map(int, input().split()))

    if n == 1:
        print("Yes")


    else:
        friend = a[-1]
        speedToBeat = max(a[:-1])

        if l != 0:
            friend = friend + k * (l - 1)

        if friend > speedToBeat:
            print("Yes")
        else:
            print("No")
