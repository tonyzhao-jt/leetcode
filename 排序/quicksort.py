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



def partition(arr, low, high):
    if low > high:
        return None
    pivot = arr[high]
    i = low
    j = high
    while i < j:
        while i < j and arr[i] <= pivot:
            i+=1
        while i < j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[high] = arr[high], arr[i]
    return i


def qs_queue(arr):
    stack = []
    low = 0
    high = len(arr) - 1
    stack.append([low, high])
    while stack:
        pair = stack.pop()
        if pair[0] >= pair[1]:
            continue
        mid = partition(arr, pair[0], pair[1])
        stack.append([mid + 1, pair[1]])
        stack.append([pair[0], mid - 1])

a = [1,4,6,2,3,5]
# quickSort(a, 0, len(a) - 1)
qs_queue(a)
print(a)


