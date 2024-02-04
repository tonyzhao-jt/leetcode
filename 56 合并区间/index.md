# 思路
根据【0】排序后比较合并。

首先排列，sort(key = lambda x:x[0])
然后合并，有两种情况
- 添加：当前 interval 左小于 merged 最右侧右值 或者 merged 为空
- 合并：其余情况