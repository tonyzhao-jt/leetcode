
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 空，则 False
        if not root:
            return False
        # 如果底下已经无值，则判断
        if not root.left and not root.right:
            return root.val == sum
        # 不然就 sum - 进行测试
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        que_node = collections.deque([root])
        que_val = collections.deque([root.val])
        while que_node:
            now = que_node.popleft()
            temp = que_val.popleft()
            # reach the end
            if not now.left and not now.right:
                if temp == sum:
                    return True
                continue
            # 左或者右边有值，则添加当前值
            if now.left:
                que_node.append(now.left)
                que_val.append(now.left.val + temp)
            if now.right:
                que_node.append(now.right)
                que_val.append(now.right.val + temp)
        return False
