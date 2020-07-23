class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, ret = [], []
        cur = root
        while stack or cur:
            # 把所有左节点入栈
            if cur:
                stack.append(cur)
                cur = cur.left
            # 没有左节点了
            else:
                # 当前出栈，加入 ret
                cur = stack.pop()
                ret.append(cur.val)
                # 查看是否有右节点
                cur = cur.right
        return ret



def inorder(root):
    stack = [], ret = []
    cur = root 
    node = None
    retRoot = None
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            if cur == None:
                node = cur
                retRoot = node # left most, new root
            else:
                ret.append(cur.val)
                cur.left = node
                node.right = cur
                node = cur
            cur = cur.right
            
    return ret