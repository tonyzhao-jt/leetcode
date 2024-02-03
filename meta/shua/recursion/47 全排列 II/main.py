class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def dfs(x):
            if x == len(nums) - 1:
                res.append(nums[:])
                return 
            used = set()
            for i in range(x, len(nums)):
                if nums[i] in used: continue 
                used.add(nums[i])
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x + 1)
                nums[i], nums[x] = nums[x], nums[i]
        
        res = []
        dfs(0)
        return res 