# 这题思路和k个链表反转还不太一样，
# 不用写sub function，会超时，因为只有一次反转，可以找到头节点就开始反转，不用找到头尾后才开始
# left和right是位置，而不是节点，也不是节点值，通过计数找位置
#  先找第一个，这个时候pre，cur一起移动，找到第一个left之后，pre不再移动
# 找到第一个之后通过计数控制反转，不用断开连接后再拼接
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None:
            return head
        dummy = ListNode(-1, head)
        pre, cur = dummy, head
        for _ in range(1, left):
            cur = cur.next
            pre = pre.next
        r_head = cur
        # cur 指针继续移动
        r_pre = None
        # 注意数字要+1，想象两个指针相邻时候，如果只进入一次反转逻辑起始相当于没有反转，这个和断开链表反转还不太一样
        for _ in range(left, right + 1):
            tmp = cur.next
            cur.next = r_pre
            r_pre = cur
            cur = tmp
        pre.next = r_pre
        r_head.next = tmp
        return dummy.next
