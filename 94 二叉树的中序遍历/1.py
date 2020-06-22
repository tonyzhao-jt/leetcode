class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, ret = [], []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ret.append( cur.val )
                cur = cur.right
        return ret