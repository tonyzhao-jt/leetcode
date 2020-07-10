class Solution:
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