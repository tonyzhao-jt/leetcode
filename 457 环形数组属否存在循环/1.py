class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next(cur: int) -> int:
            return (cur + nums[cur]) % n 

        for i, num in enumerate(nums):
            if num == 0:
                continue
            slow, fast = i, next(i)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)] > 0:
                if slow == fast:
                    if slow == next(slow):
                        nums[slow] = 0
                        break
                    return True
                slow = next(slow)
                fast = next(next(fast))
            
        return False