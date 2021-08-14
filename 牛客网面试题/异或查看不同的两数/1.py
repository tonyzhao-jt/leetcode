# 使用异或交换数
def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

def xor_judge2Num(a):
    xnet = 0
    # 先全部 ^
    for i in a:
        xnet ^= i
    # 找到那两个仅出现一次的数，他们必然有至少一位不同（1）,找到那位，以此为分组依据
    pos = 0
    while xnet >> pos & 1 != 1:
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