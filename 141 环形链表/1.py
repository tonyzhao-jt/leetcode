class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        while True:
            if not fast or not fast.next:
                return False
            fast, slow = fast.next.next, slow.next
            if fast == slow: return True