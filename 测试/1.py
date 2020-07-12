def sumtwo(start, nums, target):
    
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i-1]:
            continue
        while i < end and nums[i] + nums[end] > target:
            end -= 1
        if nums[i] + nums[end] == target:
            add

sol = Solution()
c = sol.maximumSwap(9973)
print(c)