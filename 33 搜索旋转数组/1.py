class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if target <= nums[mid] and nums[0] <= target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target >= nums[mid] and target <= nums[-1]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1