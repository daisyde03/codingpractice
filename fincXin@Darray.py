l = [[3,30,38],[44,52,54],[34,22,67]]
x = 3
flag = False
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == x:
            flag = True

if flag:
    print("found")