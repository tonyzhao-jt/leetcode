# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import SupportsComplex


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # base case 新的头节点是 head
        if not head or not head.next: return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last


class Solution:
    suc_ = None
    def reverseN(self, head, n):
        if n == 1:
            self.suc_ = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.suc_
        return last
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverseN(head,n)
        head.next = self.reverseBetween(head.next, m-1,n-1)
        return head