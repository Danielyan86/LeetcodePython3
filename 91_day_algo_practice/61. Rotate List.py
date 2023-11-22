# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur = head
        step = 0

        while cur:
            step += 1
            pre = cur
            cur = cur.next
        k %= step
        if k == 0:
            return head
        pre.next = head

        for i in range(step - k):
            pre = pre.next
        new_head = pre.next
        pre.next = None
        return new_head
