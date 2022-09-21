l = [3,1,2,5,3]
# m = [1,4,2,0,7,3]
n = len(l)
max =0
for i in range(n):
    if l[i] > max:
        max = l[i]
print(max)

for i in range(n):
    for j in range(i+1,n):
        if l[i] ==l[j]:
            print("repeating=",l[j])
for i in range(1,max):
    if i not in l:
        print("missing",i)
        