class Solution:
    def fib(self, n: int) -> int:
        x = 0
        y = 1
        z = 1
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        for i in range(n-1):
            x = y
            y = z
            z = x + y
        return z