def largestCube(a):
    min_h = min(a)
    min_idx = a.index(min_h)
    length_a = len(a)
    val_1 = min_h * length_a
    if min_idx > 0:
        val_2 = largestCube(a[:min_idx])
    else:
        val_2 = 0
    if min_idx < length_a - 1:
        val_3 = largestCube(a[min_idx + 1:])
    else:
        val_3 = 0
    return max(val_1, val_2, val_3)

testing_case = [6, 2, 5, 4, 5, 1, 6]
print(largestCube(testing_case))