l = [2,7,11,15]
target = 26

# sum = 0
for i in range(len(l)):
    sum = 0
    for j in range(i+1,len(l)):
        sum = l[i] + l[j]
        # print(sum)
        if sum == target:
            print(i,j)
