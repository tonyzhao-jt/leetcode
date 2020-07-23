import collections
class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n # init the node, -1 when no root or root
    def find(self, index):
        root = index
        while(self.parents[root] != -1):
            root = self.parents[root]
        return root # the root of the tag

    def Union(self, a, b):
        a_index = self.find(a)
        b_index = self.find(b)
        if a_index == b_index: return # same tree, no need
        self.parents[a_index] = b_index # not a same tree

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        for eq in equations:
            if eq[1] == '=': # equal cases, union
                val_1 = ord(eq[0]) - ord('a')
                val_2 = ord(eq[3]) - ord('a')
                uf.Union(val_1, val_2)
        for eq in equations:
            if eq[1] == '!': # neq cases
                val_1 = ord(eq[0]) - ord('a')
                val_2 = ord(eq[3]) - ord('a')
                if uf.find(val_1) == uf.find(val_2):
                    return False
        return True