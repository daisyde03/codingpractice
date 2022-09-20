l = [8,3,61,2,10,4,9,11,1,7,12,25,28,35]
n = len(l)
firstmax = secndmax = -234545677
for i in range(0,n):
    if (l[i] > firstmax):
        secndmax = firstmax
        firstmax = l[i]
    elif l[i] > secndmax and l[i] != firstmax:
        secndmax = l[i]

print("max =",firstmax)
# print(max)
print(secndmax)
