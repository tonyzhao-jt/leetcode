# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        p = l1 
        q = l2 
        carry = 0

        root = ListNode(0)
        s_ptr = root

        while p or q:
            val_1 = p.val if p else 0 
            val_2 = q.val if q else 0
            val = carry + val_1 + val_2
            lhs, rhs = val // 10, val % 10
            carry = lhs 
            new_node = ListNode(rhs)
            s_ptr.next = new_node
            s_ptr = s_ptr.next

            if p:
                p = p.next 
            if q:
                q = q.next 

        if carry:
            node = ListNode(carry)
            s_ptr.next = node 

        return root.next