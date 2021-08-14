class Solution:
    def reverse(self, arr, bound):
        arr_len = len(arr)
        arr_mid = len(arr) // 2
        for i in range(arr_mid):
            arr[i], arr[arr_len - 1 - i] = arr[arr_len - 1 - i], arr[i]

    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        partition_idx = k % len(nums)
        self.reverse(nums)
        self.reverse(nums[:partition_idx])
        self.reverse(nums[partition_idx:])
        return nums

sol = Solution()
print(sol.rotate([1,2,3,4,5,6,7], 3))