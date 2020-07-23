class Solution:
    # 基础的思路很简单，
    # 非障碍：等于上或者左的路径数量之和
    # 障碍：0
    # 初始化多一条边方便相加，初始化原点 dp[1][1] = 1
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]:
            return 0
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1: # origin
                    continue
                if not obstacleGrid[i-1][j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0 # obstacle

        return dp[m][n]
# 由于只考虑左上，所以 dp 可以降低1纬
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]:
            return 0
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if not obstacleGrid[i-1][j-1]:
                    dp[j] += dp[j-1]
                else:
                    dp[j] = 0 # obstacle, then all 0

        return dp[-1]