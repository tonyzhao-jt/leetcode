# 题目
深拷贝带环链表
Leetcode 环形链表 I（141） and 环形链表 II（142）
# 思路
1. 用 dict 或者 list 开拓空间判环
2. 用快慢指针和数学法（重点）
思路参考： https://blog.csdn.net/doufei_ccst/article/details/10578315


# 变式
判断无环链表是否相交
1. 先判断是否相交 （end 节点是否相同）
2. 看哪个链表更长，长的那个节点从 len_max - len_small 开始往后



# 207 Course Schedule