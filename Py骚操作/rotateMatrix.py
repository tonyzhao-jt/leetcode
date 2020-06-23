# using zip to rotate matrix
a = [
    [1,2,3],
    [2,3,4],
    [3,4,5]
]

right_rotate = list(zip(*a[::-1]))
left_rotate = list(zip(*a))[::-1]

print(left_rotate, right_rotate)