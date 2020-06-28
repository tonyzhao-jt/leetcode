class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        length = len(nums)
        for i in range(length):
            num = nums[i]
            if num <= 0 or num > length:
                nums[i] = 1
        for i in range(length):
            num = nums[i]
            idx = abs(num) - 1
            nums[idx] = -(abs(nums[idx]))
        for i in range(length):
            num = nums[i]
            if num > 0:
                return i + 1
        return length + 1
