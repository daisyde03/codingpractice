print("Hello world")
l = [1, 2, 3, 4, 5]
n = len(l)
k = []
for i in range(1, n):
    k.append(l[i])
k.append(l[0])
print(k)

t = []
temp = l[0]
for i in range(0, n-1):
    l[i] = l[i+1]
l[n-1] = temp
print(l)
