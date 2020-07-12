from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mem = defaultdict(int)
        # 记录全部的 t 中的字符
        for c in t:
            mem[c] += 1
        dis = len(t) # 得到 t 子串的大小
        min_left, min_right = 0, len(s) # 初始化最终结果数组为 len(s) + 1
        left = 0
        for right, r_c in enumerate(s):
            if mem[r_c] > 0: # 如果在 mem 中，dis - 1
                dis -= 1
            mem[r_c] -= 1 # 不论怎样都要减一，这样窗口可以往右推进
            if dis == 0: # 当前子串已经包含最小子串 t
                # min the left 左边往右移动来缩小范围
                while mem[s[left]] < 0: # 如果 mem < 0 就往右移动
                    mem[s[left]] += 1
                    left += 1 # move right

                # minimal liter drawn here
                if right - left < min_right - min_left:
                    min_right , min_left = right , left
                # 完成，把左边的再往右移动一格
                dis += 1
                mem[s[left]] += 1
                left += 1

        return "" if min_right - min_left + 1 == len(s) + 1 else s[min_left:min_right + 1]