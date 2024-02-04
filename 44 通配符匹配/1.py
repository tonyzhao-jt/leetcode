
# 字符串 s 的前 i 个字符和字符串 p 的前 j 个字符可以匹配
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # 全部初始化为负数
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # 00 匹配
        dp[0][0] = True
        # 如果字符串为空，当且仅当 p 为 *，匹配为 true
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        # 递归，当 ？ 或者字符正确匹配，为 i-1,j-1, 否则则为使用 or 不实用该 *
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                
        return dp[m][n]

# 下面这个好理解一点
# m for row (p), n for column (s)
# * 的作用是平推
# 特殊情况 s = "" 然后p 全是 *, 需要特殊处理
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        num_rows = len(p) + 1
        num_cols = len(s) + 1

        dp_table = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        dp_table[0][0] = True # the mth pattern in p match the nth token in s

        for m in range(1, num_rows):
            for n in range(1, num_cols):
                # already true and set
                if dp_table[m][n]: continue
                if p[m-1] == "*":
                    if dp_table[m-1][0]:
                        dp_table[m] = [True] * num_cols
                    if dp_table[m-1][n]:
                        for i in range(n, num_cols):
                            dp_table[m][i] = True 
                elif p[m-1] == "?" or p[m-1] == s[n-1]:
                    dp_table[m][n] = dp_table[m-1][n-1]
        
        return dp_table[-1][-1]
    

sol = Solution()