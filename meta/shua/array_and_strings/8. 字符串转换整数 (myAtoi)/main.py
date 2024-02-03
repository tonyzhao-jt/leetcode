class Solution:
    def myAtoi(self, s: str) -> int:
        # strip
        i = 0
        sign, res = 1, 0 
        while i < len(s):
            if s[i] == ' ': 
                i += 1
            else:
                break
        
        if i == len(s): return res

        if s[i] == '-':
            sign = -1 
            i += 1
        elif s[i] == '+':
            i += 1

        
        int_max, int_min = 2 ** 31 - 1, - 2 ** 31

        while i < len(s):
            if not ('0' <= s[i] <= '9'): break 
            if sign * res * 10 > int_max:
                return int_max 
            if sign * res * 10 < int_min:
                return int_min
            res = res * 10 + int(s[i])
            i += 1
        return res * sign
        