class Solution:
    def mat_mul_3(self, m_1, v_1):
        res_v = [0] * 3
        for i in range(3):
            res_v[i] = sum([m_1[i][j] * v_1[j] for j in range(3)])
        return res_v
        
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1

        init_mult = [1,1,0]

        matrix_mult = [
            [1,1,1],
            [1,0,0],
            [0,1,0]
        ]

        for _ in range(n - 2):
            init_mult = self.mat_mul_3(matrix_mult, init_mult)
        return init_mult[0]

sol = Solution()

print(sol.tribonacci(4))