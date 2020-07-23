# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    result = -sys.maxsize - 1 # minimum
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxVal(root)
        return self.result
        

    def maxVal(self, root): 
        if not root:
            return 0 
        left_val = self.maxVal(root.left)
        right_val = self.maxVal(root.right)
        val_1 = root.val
        val_2 = root.val + left_val
        val_3 = root.val + right_val
        val_4 = root.val + left_val + right_val

        maxVal = max([val_1, val_2, val_3, val_4])

        self.result = max(maxVal, self.result)
        # using the root
        return max([val_1, val_2, val_3])