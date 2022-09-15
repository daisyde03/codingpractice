vowels =['a','e','i','o','u']
s = "hello there"
v =0
c = 0
for i in range(len(s)):
    if s[i] in vowels:
        v += 1
    else:
        c += 1
print(v,c)
print("number of vowels is {} and number of consonants is {}" .format(v,c))