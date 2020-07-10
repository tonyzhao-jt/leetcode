class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        days = len(prices)
        dp = [[0]*3 for i in range(days)]
        dp[0][0] = -prices[0]
        for i in range(1, days):
            cur_price = prices[i]
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - cur_price)
            dp[i][1] = dp[i-1][0] + cur_price
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[days-1])