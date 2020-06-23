def quickSort(a, low, high):
    if low > high:
        return
    pivot = a[high]
    i = low
    j = high
    while i < j:
        while i < j and a[i] <= pivot:
            i += 1
        while i < j and a[j] >= pivot:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[i], a[high] = a[high], a[i]
    quickSort(a, low, i - 1)
    quickSort(a, i + 1, high)

a = [1,4,6,2,3,5]
quickSort(a, 0, len(a) - 1)
print(a)
