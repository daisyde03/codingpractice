l = [7, 4, 3, 9, 5, 2, 8]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            t = l[i]
            l[i] = l[j]
            l[j] = t
print(l)
