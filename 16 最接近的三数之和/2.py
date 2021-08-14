class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums = sorted(nums)
        best = 10 ** 7
        def update(s):
            nonlocal best
            if abs(s - target) < abs(best - target):
                best = s
        
        nums_len = len(nums)
        for first in range(nums_len):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second = first + 1
            third = nums_len - 1
            while second < third:
                s = nums[first] + nums[second] + nums[third]
                if s == target:
                    return target
                update(s)
                
                if s > target:
                    while second < third and nums[third-1] == nums[third]:
                        third -= 1
                    third -= 1
                else:
                    while second < third and nums[second] == nums[second + 1]:
                        second -= 1
                    second -= 1
        return best


sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], 1))