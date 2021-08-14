from typing import Collection


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mem = collections.defaultdict(int)
        for c in p:
            mem[c] += 1
        dis = len(p)
        dis_comp = len(p)
        left = 0
        res = []
        for right, val in enumerate(s):
            if mem[val] > 0:
                dis -= 1
            mem[val] -= 1
            if dis == 0:
                # move left right
                while mem[s[left]] < 0:
                    mem[s[left]] += 1
                    left += 1
                # find
                if right - left + 1 == dis_comp:
                    res.append(left)
                
                dis += 1
                mem[s[left]] += 1
                left += 1
        return res
