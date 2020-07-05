# stack
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        length = len(s)
        cur_len = 0
        max_len = 0
        for i in range(length):
            para = s[i]
            if para == '(':
                stack.append(i)
            else: # 
                stack.pop()
                if not stack: # has no value
                    stack.append(i)
                else:
                    cur_len = i - stack[-1]
                    max_len = max(max_len, cur_len)
        return max_len


# dp
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length = len(s)
        dp = [0] * length
        if length == 0: return 0
        for i in range(length):
            if s[i] == ')' and i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2
        return max(dp)