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
                ret.append(cur.val)
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