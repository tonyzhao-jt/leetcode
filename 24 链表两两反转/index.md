# 题解
直接分析最小问题。
- 只有一个 node或者没有 node 无需反转，return head
- 有两个 node, first.next = second.next, second.next = first, return second
- 又两个以上
    - 两两反转，也就是 1,2 反转 3,4 反转
    - first.next 的结果应该是 3,4 反转的结果的输出 （4）