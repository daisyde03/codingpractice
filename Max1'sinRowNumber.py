l = [[1,0,1,1],[1,1,1,1],[1,1,0,1],[0,0,0,1]]
x = 3
flag = False
max = 0
count = 0
result = -1
for i in range(len(l)):
    count = 0
    for j in range(len(l[i])):
        if l[i][j] == 1:
            count += 1
    print("count=",count)
    if count > max:
        max = count
        # print("i in ",i)
        result = i
print("max",max)
print("result = ",result)
