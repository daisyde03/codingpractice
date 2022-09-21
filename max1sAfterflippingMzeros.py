arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
m = 2

n = len(arr)
wL = wR = 0
bestWindow = 0
zeroCount = 0
while wR < n:

    if zeroCount <= m:
        if arr[wR] == 0:
            zeroCount += 1
        wR += 1

    if zeroCount > m:
        if arr[wL] == 0:
            zeroCount -= 1
        wL += 1

    if (wR - wL > bestWindow) and (zeroCount <= m):
        bestWindow = wR - wL
print(bestWindow)
# Maximum consecutive 1's'
l = [1, 0, 0, 1, 1,1,1,1,1, 0, 1, 0, 1, 1, 1]
n = len(l)
count = 0
max = 0
for i in range(n):
    if l[i] == 1:
        count += 1
    if count > max:
        max = count
    if l[i] == 0:
        count = 0
print(max)