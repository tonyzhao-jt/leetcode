# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        fast, slow, first_ = head, head, head
        for i in range(k - 1):
            fast = fast.next
            first_ = first_.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        tmp = first_.val
        first_.val = slow.val
        slow.val = tmp

        return head