# 解题
这个最大的发现是。如果 用 for i in range(k) 实际上停止的位置是在 k+1 个 node 上
经过到顶操作后，前面是倒数第 n + 1 个值 （.next 指向倒数第 n 个 node）
- 如果想指向第 n 个 node 的话。 for i in range(k-1)