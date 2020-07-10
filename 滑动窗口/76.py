from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mem = defaultdict(int)
        # interate t to login
        for c in t:
            mem[c] += 1
        dis = len(t) # the distance keeping the value
        min_left, min_right = 0, len(s)
        left = 0
        for right, r_c in enumerate(s):
            if mem[r_c] > 0: # charatcer in t
                dis -= 1
            mem[r_c] -= 1
            if dis == 0: # all character in t is now in the min_liter
                # min the left
                while mem[s[left]] < 0: # the character that not in the t
                    mem[s[left]] += 1
                    left += 1 # move right

                # minimal liter drawn here
                if right - left < min_right - min_left:
                    min_right , min_left = right , left
                # move speacial left( in t)
                dis += 1
                mem[s[left]] += 1
                left += 1

        return "" if min_right - min_left + 1 == len(s) + 1 else s[min_left:min_right + 1]