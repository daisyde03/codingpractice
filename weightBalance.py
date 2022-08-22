t = int(input())
for i in range(t):
    w1,w2,x1,x2,m = map(int, input().split())
    d = w2 - w1
    mi = m*x1
    ma = m*x2
    if (d >= mi and d <= ma):
        print(1)
    else:
        print(0)