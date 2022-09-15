#anagram
str1 = "string"
str2 = "length"
# anagramstat = False
if len(str1) != len(str2):
    print(str1,str2, "are not anagram")
st1 = ''.join(sorted(str1))
print(st1)
st2 = ''.join(sorted(str2))
print(st2)
# anagramstat = st1._eq_.(st2)
if st1.lower() == st2.lower():
    print("anagram")
else:
    print("not anagram")
