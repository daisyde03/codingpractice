print("Hello world")
word = "geeEEkksseellEE"
li = []
for i in word:
    li.append(i)
print(li)
d = (1, 1, 2, 2, 3, 3, 3, 6, 4, 2)
frequency = {}
x = len(d)
print(x)
# count =0
for i in li:
    if i in frequency:
        frequency[i] += 1

    else:
        frequency[i] = 1
print(frequency)

word = "geeEEkksseellEE"
s = set(word)

st = ''
for i in s:
    count = 0
    for j in word:
        if i == j:
            count += 1
    print("count of {} is {}".format(i, count))
    st = st + i + str(count)
print(st)

Hello world
count of k is 2
count of l is 2
count of e is 4
count of E is 4
count of s is 2
count of g is 1
k2l2e4E4s2g1
