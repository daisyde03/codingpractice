def mergeSort(a):
    if len(a) > 1:
        r = len(a) // 2
        l = a[:r]
        print("l=", l)
        m = a[r:]
        print("m=", m)

        mergeSort(l)
        mergeSort(m)

        i = j = k = 0
        while i < len(l) and j < len(m):
            if l[i] < m[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = m[j]
                j += 1

            k += 1

        while i < len(l):
            a[k] = l[i]
            i += 1
            k += 1
        while j < len(m):
            a[k] = m[j]
            j += 1
            k += 1


def printList(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print()


a = [5, 8, 7, 1, 4, 3, 2]
mergeSort(a)
printList(a)

