class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        length_A = len(A)
        length_B = len(B)
        # dp[i][j] 代表 B[:i] 和 A[:j] 字符串的最大公共子数组
        dp_ = [[0] * (length_A + 1) for _ in range(length_B + 1)] # 初始化为 0
        res = 0
        for i in range(1, length_A + 1):
            for j in range(1, length_B + 1):
                if A[i - 1] == B[j - 1]: # 如果相等，则为之前的 dp[i-1][j-1] + 1
                    dp_[i][j] = dp_[i - 1][j - 1] + 1
                    res = max(dp_[i][j], res) # 更新结果
        
        return res
