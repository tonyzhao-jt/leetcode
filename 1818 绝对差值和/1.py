
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        total = 0
        sl = sorted(nums1)
        ans = inf

        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            total += diff

            left, right = 0, n-1
            while left < right:
                mid = left + right >> 1
                if sl[mid] < nums2[i]:
                    left = mid + 1
                else:
                    right = mid
            
            ans = min(ans, abs(sl[left] - nums2[i]) - diff)
        return (total + ans) % (10 ** 9 + 7) if total else total
