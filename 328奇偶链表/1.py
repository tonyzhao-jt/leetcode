
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return head
        odd = head 
        even_head = even = head.next
        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head