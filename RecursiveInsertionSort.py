def recInsertion(l, n):
    if n <= 1:
        return

    recInsertion(l, n - 1)
    last = l[n - 1]
    # print("last =",last,end=" ")
    j = n - 2
    # print("j =", j,end=" ")
    # print("l[j]=",l[j])
    while (j >= 0 and l[j] > last):
        l[j + 1] = l[j]
        j -= 1
        # print(l)
    l[j + 1] = last
    # print("outsidewhileloop",l)

def printArr(l, n):
    for i in range(n):
        print(l[i], end=" ")


l = [2, 5, 9, 1]
n = len(l)
recInsertion(l, n)
printArr(l, n)