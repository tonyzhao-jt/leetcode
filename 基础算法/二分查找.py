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
arr = [ 2, 3, 4, 10, 40 ]

print(binarySearch(arr, 0, len(arr) - 1, 3))