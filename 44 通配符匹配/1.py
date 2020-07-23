

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
