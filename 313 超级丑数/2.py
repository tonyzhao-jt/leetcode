class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int: 
        
        length = len(primes)
        pointers = [1] * length
        dp = [inf] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = min(dp[pointers[j]] * primes[j] for j in range(length))
            # update pointers
            for j in range(length):
                if dp[pointers[j]] * primes[j] == dp[i]:
                    pointers[j] += 1
        
        return dp[n]


sol = Solution()
res = sol.nthSuperUglyNumber(12, [2,7,13,9])
print(res)