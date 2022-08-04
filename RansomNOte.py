#Problrm statement
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#https://leetcode.com/problems/ransom-note/

# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         rlen = len(ransomNote)
#         mlen = len(magazine)
#         result =False

#         for i in ransomNote:
#             valueofRansomNote = ransomNote.count(i)
#             valueofMagazine = magazine.count(i)
#             if 1<=valueofRansomNote<=valueofMagazine:
#                 result =True
#             else:
#                 result = False
#         return result
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = {}
        rLen, mLen = len(ransomNote), len(magazine)
        for ch in magazine:
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1
        for ch in ransomNote:
            if ch not in counts:
                return False
            counts[ch] -= 1
            if counts[ch] < 0:
                return False

        return True
obj = Solution()
r="aa"
m="ab"
print(obj.canConstruct(r,m))