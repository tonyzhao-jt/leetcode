class Solution:
    def partition(self, arr, l, r):
        if l > r:
            return None
        pivot = arr[r]
        i = l
        j = r

        while i < j:
            while i < j and arr[i] <= pivot:
                i += 1
            while i < j and arr[j] >= pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[i], arr[r] = arr[r], arr[i]
        return i
    def getLeastNumbersK(self, arr, l, r, k):
        idx = self.partition(arr, l, r)
        if idx == k:
            return arr[idx]
        elif idx < k:
            return self.getLeastNumbersK(arr, idx + 1, r, k)
        else:
            return self.getLeastNumbersK(arr, l, idx - 1, k)

    def getLeastNumbers(self, arr, k):
        l = 0
        r = len(arr) - 1
        # k = len(arr) - k
        val = self.getLeastNumbersK(arr, l, r, k)
        return val


arr = [3,1,2,4]
k = 2

sol = Solution()
print(sol.getLeastNumbers(arr, k))