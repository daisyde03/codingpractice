l = [8,3,6,2,10,4,9]
n = len(l)
max = l[0]
for i in range(0,n-1):
    # print(l[i])
    if (l[i] > max):
        max = l[i]
print(max)
