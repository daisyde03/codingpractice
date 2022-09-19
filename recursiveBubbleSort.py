def recBubbleSort(l):
    i = 0

    for j in range(0, len(l) - 1):
        if l[j] > l[j + 1]:
            temp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = temp
            i += 1
    if i == 0:
        return l
    else:
        recBubbleSort(l)


l = [1, 5, 8, 3, 2, 11, 7, 4]
recBubbleSort(l)
print(l)