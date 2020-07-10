def fib(n):
    x = 0
    y = 1
    z = 1
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    for i in range(2, n):
        x = y
        y = z
        z = x + y
    return z

def fib2(n):
    x = 0
    y = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(1, n):
        z = x + y
        x = y
        y = z
    return z

# a = fib2(10)
# print(a)

def judge1(n):
    length = len(str(n))
    num = 0 
    for pos in range(length):
        if n >> pos & 1 == 1:
            num += 1

    return num
# judge1(101)
# 快速幂
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0: x, n = 1/x, -n
        res = 1
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res

# 终止条件在 p and q == None and p.val != q.val
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q:
            return p == None and q == None
        if (p.val != q.val):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

class Solution:
    def isSameTree(self, a, b):
        if not b:
            return True
        if not a:
            return False
        if a.val != b.val:
            return False
        return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False # none will not happen in this case
        if self.isSameTree(A, B):
            return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

# 33
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        stack, root = [], float('+inf')
        for i in range(len(postorder) - 1, -1, -1):
            cur_node = postorder[i]
            if cur_node > root: return False
            while stack and cur_node < stack[-1]:
                root = stack.pop()
            stack.append(cur_node)
        return True