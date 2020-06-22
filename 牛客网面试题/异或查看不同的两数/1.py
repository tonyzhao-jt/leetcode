# 使用异或交换数
# a = 1
# b = 2
# a = a^b
# b = a^b
# a = a^b
# print(a, b)
def xor_judge2Num(a):
    xnet = 0
    for i in a:
        xnet ^= i
    pos = 0
    while xnet >> pos & 1 != 1: # find the first 1 position
        pos += 1
    num1, num2 = 0, 0
    for el in a:
        if (el >> pos & 1) == 1:
            num1 ^= el
        else:
            num2 ^= el
    return num1, num2

test = [1,1,5,2,4,2,3,3]
print(xor_judge2Num(test))