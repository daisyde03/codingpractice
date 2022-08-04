#problem statement

#You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
#A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
#https://leetcode.com/problems/richest-customer-wealth/
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealthList=[]
        for i in accounts:
            currentwealth=0
            for j in i:
                currentwealth += j
            wealthList.append(currentwealth)
        return(max(wealthList))


# class Solution:
#     def maximumWealth(self, accounts):
#         """
#         :type accounts: List[List[int]]
#         :rtype: int
#         """
#         maxwealth = 0
#         for i in accounts:
#             currentwealth = 0
#             for j in i:
#                 currentwealth += j
#             maxwealth = max(maxwealth, currentwealth)
#         return (maxwealth)


obj = Solution()
account=[[1,2,3],[2,3,4],[3,4,5]]
#print(account)
print(obj.maximumWealth(account))