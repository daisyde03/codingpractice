# problem statement
# https://practice.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=array-of-alternate-ve-and-ve-nos
l = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
positive = []
negative = []
formatted = []
for i in range(len(l)):
    if l[i] < 0:
        negative.append(l[i])
    else:
        positive.append(l[i])
while positive or negative:
    if len(positive):
        formatted.append(positive.pop(0))
    if len(negative):
        formatted.append(negative.pop(0))


print(formatted)
