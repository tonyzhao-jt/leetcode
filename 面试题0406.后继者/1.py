class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root: return None
        # 如果当前值小于 p，那必定在右侧
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        # 当前值大于 p，则有可能是当前值，也有可能是下一个节点的右侧节点
        else:
            return self.inorderSuccessor(root.left, p) or root