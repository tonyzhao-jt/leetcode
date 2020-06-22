class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = head
        j = head
        for z in range(n):
            j = j.next
        if j == None: return head.next
        while j.next != None:
            j = j.next
            i = i.next
        # now i on the lst  n + 1 node
        i.next = i.next.next
        return head