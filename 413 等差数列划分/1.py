class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        pre = 0
        count = 0
        diff = nums[1] - nums[0]
        for i in range(2, len(nums)):
            if diff == nums[i] - nums[i-1]:
                pre += 1
                count += pre
            else:
                diff = nums[i] - nums[i-1]
                pre = 0
        return count
        