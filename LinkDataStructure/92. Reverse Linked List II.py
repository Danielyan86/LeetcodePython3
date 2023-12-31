# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 这题思路和k个链表反转还不太一样，
# 不用写sub function，会超时，因为只有一次反转，可以找到头节点就开始反转，不用找到头尾后才开始
# left和right是位置，而不是节点，也不是节点值，通过计数找位置
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or head.next is None:
            return head
        dummy_h = ListNode(0, head)
        pre, cur = None, dummy_h
        for _ in range(left):
            pre = cur
            cur = cur.next
        l_start = cur
        pre1 = None  # 设置临时指针，方便反转链表用
        for _ in range(right - left + 1):  # 需要注意+1
            tmp = cur.next
            cur.next = pre1
            pre1 = cur
            cur = tmp
        pre.next = pre1
        l_start.next = tmp
        return dummy_h.next
