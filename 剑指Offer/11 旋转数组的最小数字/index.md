# 题目
旋转数组的最小数字
# 思路
二分法
- 在最小值左右侧的都大于它
- 左边的数大于右侧数的最大值
- 如果 numbers[pivot] < numbers[high] ，则在左侧
- 如果 numbers[pivot] > numbers[high] 则在右侧
- == 则去掉high 点
