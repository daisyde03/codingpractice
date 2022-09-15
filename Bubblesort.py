l = [1, 2, 5, 3, 6, 7, 9]
for i in range(len(l)):
    for j in range((len(l) - i - 1)):
        if l[j] > l[j + 1]:
            t = l[j]
            l[j] = l[j + 1]
            l[j + 1] = t
print(l)
