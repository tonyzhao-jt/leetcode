# 题目
超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。

给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。

题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 题解
主要是这个丑数的定义
- 最小堆
    - 每次取出堆顶数
    - 和 prime list 相乘，加入 seen
    - 取 n 次就是结果
- DP
    - pointers & prime
    - pointer 指到 dp 上面，本质上 pointer + 1 的过程是让某个质数对应的乘数变大的过程
    - 第二个 for 不能省略，会出现两个都相等的情况