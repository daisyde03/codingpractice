l = [2,3,5,1,9]
n = len(l)
k =10
maxlength =0
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum = sum + l[j]
        if sum ==k:
            maxlength =max(maxlength,(j-i+1))
print(maxlength)
