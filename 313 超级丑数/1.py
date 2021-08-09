# 最小堆
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int: 
        seen = {1}
        heap = [1]

        for i in range(n):
            ugly = heapq.heappop(heap)
            for prime in primes:
                ugly_new = prime * ugly
                if ugly_new not in seen:
                    seen.add(ugly_new)
                    heapq.heappush(heap, ugly_new)
        return ugly

