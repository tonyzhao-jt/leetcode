from typing import Optional, List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # special cases
        if not nums or n < 3:
            return []
        
        nums.sort()
        ans = nums[0] + nums[1] + nums[2] # init 
        
        for i in range(n - 2):
            # remove the repeating cases
            if i>= 1 and nums[i] == nums[i-1]: continue 
            L, R = i + 1, n - 1 
            while L < R:
                sum_three = nums[i] + nums[L] + nums[R]
                if abs(sum_three - target) < abs(ans - target):
                    ans = sum_three
                if sum_three - target > 0:
                    R -= 1
                elif sum_three - target < 0:
                    L += 1
                else:
                    return target

        return ans