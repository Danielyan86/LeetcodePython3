# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next == None or right == left:
            return head
        dummy_h = ListNode(None, head)
        pre, cur = dummy_h, head
        # 刚开始想复杂了通过简单循环计数就能找到边界，不用做复杂判断
        # 思路不复杂，但是需要注意细节问题，需要搞清楚翻转链表的起始点

        for _ in range(left - 1):
            pre, cur = pre.next, cur.next
        l_start = pre
        revered_end = cur
        pre, cur = pre.next, cur.next
        for _ in range(right - left):
            pro_tmp = cur.next
            cur.next = pre
            pre = cur
            cur = pro_tmp
        revered_end.next = cur
        l_start.next = pre
        return dummy_h.next
