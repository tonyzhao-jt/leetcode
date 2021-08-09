def binarySearch(arr, l, r, x):
    if r >= l:
        mid = (l + r) // 2
    
    if arr[mid] == x:
        return mid
    elif arr[mid] >= x:
        return binarySearch(arr, l , mid - 1, x)
    else:
        return binarySearch(arr, mid + 1 , r, x)
    return - 1

def binarySearchWithBitwidth(arr, l, r, x):
    while l < r:
        mid = l + r >> 1
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l
arr = [ 2, 3, 4, 10, 40 ]

print(binarySearch(arr, 0, len(arr) - 1, 3))
print(binarySearchWithBitwidth(arr, 0, len(arr) - 1, 8))