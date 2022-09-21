l = [1,2,3,4,5,6]
n = len(l)
temp = []
k =2
for i in range(k,n):
    temp.append(l[i])
print(temp)
for i in range(k):
    temp.append(l[i])
print(temp)

# add all the zeros at the end of the array

l = [1, 0, 3, 0, 0, 6]
n = len(l)
temp = []
temp2 = []
k = 2
for i in range(0, n):
    if l[i] >= 1:
        temp.append(l[i])
    else:
        temp2.append(l[i])

print(temp)
print(temp2)
for i in range(len(temp2)):
    temp.append(temp2[i])
# temp.append(temp2)
print(temp)