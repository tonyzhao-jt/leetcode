# 这个 file 用来时常练习 quicksort
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
    quickSort(a, low ,i - 1)
    quickSort(a, i + 1, high)


a = [1,3,2,4]
quickSort(a, 0, len(a) - 1)
print(a)