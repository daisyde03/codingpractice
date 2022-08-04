#problem statement
#Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
#https://leetcode.com/problems/fizz-buzz/

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a=[]
        for i in range(1,n+1):
            divisible_by_3 = (i % 3 == 0)
            divisible_by_5 = (i % 5 == 0)
            i_as_string =""
            if divisible_by_3:
                i_as_string += "Fizz"
            if divisible_by_5:
                i_as_string += "Buzz"
            # if (divisible_by_3 && divisible_by_5):
            #     i_as_string += "FizzBuzz"
            if not i_as_string:
                i_as_string= str(i)
            a.append(i_as_string)
        return a

obj= Solution()
n=15
print(obj.fizzBuzz(n))