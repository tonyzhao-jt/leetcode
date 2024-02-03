class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, used, depth, size, path, res):
            if depth == size:
                res.append(path[:])
                return 
            
            for i in range(size):
                if used[i] == 0:
                    # dfs, try use this node
                    used[i] = 1 
                    path.append(nums[i])
                    dfs(nums, used, depth + 1, size, path, res)
                    # this node's search is finished
                    used[i] = 0
                    path.pop()
        


        if len(nums) == 0:
            return []
        
        # dfs 
        used = [0 for _ in range(len(nums))]
        res = []
        # dfs, depth, size, res
        dfs(nums, used, 0, len(nums), [], res)
        return res 