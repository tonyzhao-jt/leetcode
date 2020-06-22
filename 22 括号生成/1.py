class Solution:
    def generateParenthesis(self, n):
        self.ava_list = [] # generated available list
        self.gp(n, n, '')
        return self.ava_list
    def gp(self, left, right, cur_str):
        if left < 0 or right < 0 or left > right:
            return 
        if left == 0 and right == 0:
            self.ava_list.append(cur_str)
        self.gp(left - 1, right, cur_str + '(')
        self.gp(left, right - 1, cur_str + ')')

sol = Solution()
r = sol.generateParenthesis(3)
print(r)