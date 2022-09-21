l = [1, 2, 3, 7, 4, 8, 9, 10, 11, 12, 25, 25, 28, 61]
fl = False
for i in range(1,len(l)):
    if l[i] < l[i-1]:
        fl = True
    else:
        fl = False
if fl:
    print("sorted")
else:
    print("not sorted")