# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
word = "geeEEkksseellEE"
s = set(word)

st = ''
max1 = 0
min1 = 1
maxe = ''
mine = ''
for i in s:
    count = 0

    for j in word:
        if i == j:
            count += 1
            if count >= max1:
                max1 = count
                maxe = j
            if count <= min1:
                min1 = count
                mine = j
    print("count of {} is {}".format(i, count))
    st = st + i + str(count)
print(st)
print("max frequecy", maxe, max1)
print("min frequency", mine, min1)

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
word = "geeEEkksseellEE"
# s = set(word)
# sortd = ''.join(sorted(word))
# print(sortd)
# l = list(sortd)
m = list(word)
m.sort()
print(m)
# print(l)
# l.sort()
# print(l)
# s = set(sortd)
# print(s.sort())

st = ''
max1 = 0
min1 = 1
maxe = ''
mine = ''
for i in m:
    count = 0

    for j in m:
        if i == j:
            count += 1
            if count >= max1:
                max1 = count
                maxe = j
            if count <= min1:
                min1 = count
                mine = j
    print("count of {} is {}".format(i, count))
    st = st + i + str(count)
print(st)
print("max frequecy", maxe, max1)
print("min frequency", mine, min1)


