class Solution:
    def lengthOfLongestSubstring(self, s):
        # i is the start of the longest words
        # j is the end of the lingest words
        
        st = {} # the character sets
        i, ans = -1,0 # i is the lower bound, ans is the word's length
        
        for j in range(len(s)): # j is the upper bound
            if s[j] in st: # when the chacter j is appeared in the string before
                i = max(st[s[j]], i) # update the i's bound
            ans = max(ans, j - i) # update length of the longest character
            st[s[j]] = j # update the upper bound
        return ans
            