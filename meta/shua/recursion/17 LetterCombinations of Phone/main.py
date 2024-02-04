class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mapper = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtracking(comb, index):
            if index == len(digits):
                res.append(comb)
                return 
            candidates = mapper[digits[index]]
            for letter in candidates:
                backtracking(comb + letter, index + 1)
        
        res = []
        backtracking('', 0)
        return res 