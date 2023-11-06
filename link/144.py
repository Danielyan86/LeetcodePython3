# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        # 注意边界值
        if head.next is head:
            return True
        # 注意快慢指针顺序
        sp = head
        fp = head.next
        while fp and fp.next:
            if fp == sp:
                return True
            fp = fp.next.next
            sp = sp.next

        return False
