from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # special case judgement
        n = len(nums)
        if not n or n < 3:
            return []
        
        res = []
        nums.sort()
        for idx in range(n-2):
            val = nums[idx]
            if val > 0: return res 
            if idx >= 1 and nums[idx-1] == val: continue # remove the repeat result (need to >= 1, be careful)
            # L R (double pointer)
            # move L right make the L pointed value bigger
            # move R left make the R pointed value smaller
            L = idx + 1 
            R = n - 1
            while L < R:
                if nums[L] + nums[R] + val == 0:
                    res.append([nums[L], nums[R], val])
                    # pass the repeating elements
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1 
                elif nums[L] + nums[R] + val < 0:
                    # make it bigger
                    L += 1
                    continue
                else:
                    R -= 1
                    continue
        
        return res 

sol = Solution()
res = sol.threeSum([0,0,0,0])
print(res)