#problem statement
#https://www.codechef.com/submit/CABS?tab=statement


t = int(input())
for x in range(t):
    A,B = map(int, input().split())
    if A > B:
        print("FIRST")
    elif B > A:
        print("Second")
    elif A==B:
        print("ANY")