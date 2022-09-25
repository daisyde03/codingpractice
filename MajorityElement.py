#problem statement
#https://takeuforward.org/data-structure/find-the-majority-element-that-occurs-more-than-n-2-times/

l = [2,2,1,1,1,2,2]
n = len(l)
maxm = 0
index = -1
for i in range(n):
    count = 0
    for j in range(n):
        if l[i] == l[j]:
            count += 1
    if count > maxm:
        maxm = count
        index = i
if maxm >= n//2:
    print(l[index])
