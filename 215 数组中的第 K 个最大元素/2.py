class Solution:
    def partition(self, a, low, high):
        if low > high:
            return None
        pivot = a[high]
        i, j = low, high
        while i < j:
            while i < j and a[i] <= pivot:
                i += 1
            while i < j and a[j] >= pivot:
                j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
        a[i], a[high] = a[high], a[i]
        return i
    def findKthlargestT(self, nums, low, high, k):
        idx = self.partition(nums, low, high)
        if idx == k:
            return nums[k]
        elif idx < k:
            return self.findKthlargestT(nums, idx + 1 , high, k)
        else:
            return self.findKthlargestT(nums, low , idx - 1, k)

    def findKthLargest(self, nums, k: int) -> int:
        low, high = 0, len(nums) - 1
        return self.findKthlargestT(nums, low, high, len(nums) - k)

sol = Solution()
array = [3,1,2,4]
idx = 2

print(sol.findKthLargest(array, idx))