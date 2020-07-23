class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        big = 10 ** 9
        m = len(dungeon)
        n = len(dungeon[0])
        # 初始化为 big
        dp = [[big] * (n + 1) for _ in range(m + 1)]
        # 目标点的左侧和上侧初始化为 1
        dp[m][n-1] = dp[m-1][n] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                minn = min(dp[i+1][j], dp[i][j+1])
                # 左上小的那个 - 当前区域的值
                dp[i][j] = max(minn - dungeon[i][j], 1)
        return dp[0][0]

