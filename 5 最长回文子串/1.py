# 抄答案了，边界写不好
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 1:
            return ""

        def expandAroundCenter(left, right):
            L, R = left, right
            while L >= 0 and R <len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            return R - L - 1

        left, right = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(i, i) # 奇数
            len2 = expandAroundCenter(i, i+1) # 偶数
            max_len = max(len1, len2)
            if max_len > right - left:
                left = i - (max_len - 1)//2
                right = i + max_len//2
        return s[left:right+1]