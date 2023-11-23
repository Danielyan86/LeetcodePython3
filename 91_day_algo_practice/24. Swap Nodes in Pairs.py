# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0, head)
        pre, cur = dummy, head

        # if current node is None or next is None, then end loop
        while cur and cur.next:
            next = cur.next
            next_tmp = next.next
            pre.next = next
            next.next = cur
            cur.next = next_tmp
            pre = cur
            cur = next_tmp
        return dummy.next
