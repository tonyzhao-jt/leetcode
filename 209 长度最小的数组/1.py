class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        start, end = 0, 0
        n = len(nums)
        min_length = n + 1
        sum_now = 0
        while end < n:
            sum_now += nums[end]
            while sum_now >= s:
                min_length = min(min_length, end - start + 1)
                sum_now -= nums[start]
                start += 1
            end += 1
        return 0 if min_length == n + 1 else min_length
            

# 几个注意的地方
# 先动 end, 再动 start 
# 结果是 end - start + 1