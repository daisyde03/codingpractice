l = [1,0,3,0,0,6]
m = [1,4,2,0,7,3]
n = len(l)
union = []
common = []
intersection =[]
for i in range(len(l)):
    for j in range(len(m)):
        if l[i] == m[j]:
            intersection.append(l[i])
print("intersection=",set(intersection))
for i in range(len(l)):
    for j in range(len(m)):
        if l[i] != m[j]:
            union.append(l[i])
            union.append(m[j])
print("Union =",set(union))

union.append(common)
