# 题目
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
- EN: Longest Substring Without Repeating Characters 

# 做法
滑动窗口
1. 用一个下标 i 表示当前观测的sequence 的起点，和结果 ans 存储最大值
2. 用一个 dict （hashtable） 存储当前的字符串的最后一次出现的索引
3. 遇到之前出现的字符之后，更新观测位置到 seq_i max(i, st[s[j]])
4. 不断计算当前观测 seq 的长度
5. 将当前 character 的 index 存入 dict （可以是存在的或者是不存在的）

关于写法
- 这种写法巧妙的用两个 max 解决了判断 string 的位置
- 后出现的 string 会出现在 i 的后面，改变 ans 而先出现的则会出现在 i 的前面，不影响到 ans 的改变