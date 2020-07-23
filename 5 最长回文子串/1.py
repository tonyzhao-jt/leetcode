# 抄答案了，边界写不好
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        # 如果不是 s 或者 < 1，那就不是
        if not s or len(s) < 1:
            return ""
        # 往两侧扩展
        def expandAroundCenter(left, right):
            L, R = left, right
            while L >= 0 and R <len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            return R - L - 1
        # 简单来说就是遍历，同时中间向两侧扩展
        left, right = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(i, i) # 奇数
            len2 = expandAroundCenter(i, i+1) # 偶数
            # 更新 max
            max_len = max(len1, len2)
            if max_len > right - left:
                left = i - (max_len - 1)//2
                right = i + max_len//2
        return s[left:right+1]