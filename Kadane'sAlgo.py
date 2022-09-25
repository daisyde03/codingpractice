#problem statement
#https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/

l = [-2,1,-3,4,-1,2,1,-5,4]
subarray =[]
length = len(l)
maxsofar = -1
currentmax = 0
s = start = end = 0

for i in range(length):
    currentmax += l[i]
    if maxsofar < currentmax:
        subarray.clear()
        maxsofar = currentmax
        # subarray.append(l[])
        start = s
        end = i
        subarray.append(l[start])
        subarray.append(l[end])
    if currentmax < 0:
        currentmax = 0
        s = i+1

print(subarray)
print(maxsofar,start,end)
for i in range(start,end):
    print(l[i])



#problem statement
# https://practice.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/0?category=&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=max-sum-in-sub-arrays
l = [4, 3, 1, 5, 6]
result = 0
for i in range(0,len(l)-1):
    print(l[i],l[i+1])
    result = max(result,l[i]+l[i+1])
    print(result)

# problem statement
# https://takeuforward.org/data-structure/stock-buy-and-sell/

l = [4, 3, 1, 5, 6]
maxpro = 0
for i in range(len(l)):
    # maxpro = 0
    for j in range(i+1,len(l)):
        if l[i] < l[j]:
            maxpro = max(maxpro,l[j]-l[i])
            # print(i,j)
            print(l[i],l[j])
            print(maxpro)
print(maxpro)
