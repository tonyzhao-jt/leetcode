class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            nums = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    nums += i + 1
                    j += 1
                else:
                    i -= 1 # move upper
            return nums >= k
        
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

