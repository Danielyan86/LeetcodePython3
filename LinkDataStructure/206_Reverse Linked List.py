# reversing a single list needs 3 ponits and 4 steps
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        if head.next is None:
            return head
        pre, cur = head, head.next
        pre.next = None
        while cur:
            pro = cur.next
            cur.next = pre
            pre = cur
            cur = pro

        return pre
