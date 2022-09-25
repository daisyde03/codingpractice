l = [2,1,0,0]
count_0 = count_1 = count_2 = 0
temp = []
# sum = 0
for i in range(len(l)):
    if l[i] == 0:
        count_0 += 1
    elif l[i] == 1:
        count_1 += 1
    else:
        count_2 += 1
print(count_0,count_1,count_2)

for i in range(len(l)):
    if i < count_0:
        temp.append(0)
for i in range(len(l)):
    if i < count_1:
        temp.append(1)
for i in range(len(l)):
    if i < count_2:
        temp.append(2)
print(temp)
m = [2,1,0,0]
r = len(m)-1
le = mid = 0
while (mid <= r):
    if m[mid] == 0:
        m[le],m[mid] = m[mid], m[le]
        le += 1
        mid += 1
    if m[mid] == 1:
        mid += 1
    if m[mid] == 2:
        m[mid], m[r] = m[r], m[mid]
        r -= 1
print(m)
