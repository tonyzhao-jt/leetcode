class Solution:
    def countAndSay(self, n: int) -> str:
        # only is to create the countAndSay n
        if n == 1: return "1"
        s = '1'
        res = ""
        for i in range(n - 1):
            L, R = 0, 0
            # create all comb like str(#) + str(val)
            while R <= len(s) - 1:
                while R <= len(s) - 1 and s[L] == s[R]: R += 1
                cnt = R - L 
                res += str(cnt) + s[L]
                L = R 
            s = res[:]
            res = ""
        return s