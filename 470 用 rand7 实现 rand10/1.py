# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            a = rand7()
            b = rand7()
            num = (a - 1) * 7 + b # 49
            
            if num <= 40: return num % 10 + 1 # 

            # 下面是优化，利用被抛弃的数字
            a = num - 40 # rand 9
            b = rand7()
            num = (a - 1) * 7 + b # rand 63
            if num <= 60: return num % 10 + 1

            a = num - 60 # rand3
            num = (a-1) * 7 + rand7()
            if num <= 20: return num % 10 + 1


