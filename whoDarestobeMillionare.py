#problem statement
#https://www.codechef.com/submit/WDTBAM
T = int(input())
for w in range(T):
    N = int(input())
    correct = input()
    chef = input()
    prize = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if correct[i] == chef[i]:
            count += 1
    if count == N:
        print(prize[-1])
    else:
        print(max(prize[:count + 1]))
