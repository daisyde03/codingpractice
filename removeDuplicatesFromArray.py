l = [8,3,1,61,2,10,4,9,11,1,7,12,25,28,25]
n = len(l)
for i in range(n):
    for j in range(n-i-1):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp
print(l)
init = l[0]
myset = set()
for i in range(n):
    myset.add(l[i])
print(myset)
n = len(myset)
print(n)
li = list(myset)
print("list",li)
