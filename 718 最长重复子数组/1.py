class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        length_A = len(A)
        length_B = len(B)
        dp_ = [[0] * (length_A + 1) for _ in range(length_B + 1)]
        res = 0
        for i in range(1, length_A + 1):
            for j in range(1, length_B + 1):
                if A[i - 1] == B[j - 1]:
                    dp_[i][j] = dp_[i - 1][j - 1] + 1
                    res = max(dp_[i][j], res)
        
        return res