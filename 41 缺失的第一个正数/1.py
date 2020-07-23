class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 先扫描 1
        if 1 not in nums:
            return 1
        length = len(nums)
        # 把所有 <= 1 的值都变成 1
        for i in range(length):
            num = nums[i]
            if num <= 0 or num > length:
                nums[i] = 1
        # 扫描一次数组标记槽为 -abs
        for i in range(length):
            num = nums[i]
            idx = abs(num) - 1
            nums[idx] = -(abs(nums[idx]))
        # 最后扫描一次，如果发现 > 0 的值，就是第一个缺失的正整数
        for i in range(length):
            num = nums[i]
            if num > 0:
                return i + 1
        return length + 1
