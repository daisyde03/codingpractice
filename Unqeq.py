#problem statement
#https://www.codechef.com/submit/UNQEQ?

t = int(input())
for i in range(t):
    n = int(input())
    if n % 4 != 0:
        print('NO')

    else:
        print('YES')
        p = []
        q = []
        for i in range(n // 4):
            p.append(1 + 2 * i)
            q.append(2 + 2 * i)
        for i in range(n // 4):
            p.append(n // 2 + 2 + 2 * i)
            q.append(n // 2 + 1 + 2 * i)
        print(*p)