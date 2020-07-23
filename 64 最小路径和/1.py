class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return False
        
        width = len(grid[0])
        height = len(grid)

        big = 9999

        dp = [[big for i in range(width + 1)] for _ in range(height + 1)]
        dp[1][1] = grid[0][0]
        for i in range(1, height + 1):
            for j in range(1, width + 1):
                if i == 1 and j == 1:
                    continue
                dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[height][width]