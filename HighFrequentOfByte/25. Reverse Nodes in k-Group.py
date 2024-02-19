# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 先写反转函数，注意先把尾巴节点断开，指向None，这样就和正常的一维数组反转一样了
# 反转函数返回的头和尾节点和传入的是相反的
# 外层函数，如果不够 K个节点，直接返回，注意判断条件
# 注意在调用反转函数之前保存下个节点，原理和单链表反转一样


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_link(head, tail):
            tail.next = None
            pre, cur = None, head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre, head

        if head.next is None:
            return head
        dummy_h = ListNode(0, head)
        pre = cur = dummy_h
        while cur:
            for _ in range(k):
                cur = cur.next  # 先移动，再判断
                if cur is None:
                    return dummy.next
                cur = cur.next
            tmp = cur.next
            h, t = reverse_link(pre.next, cur)
            pre.next = h
            t.next = tmp
            pre = cur = t  # 指向新的起点，也就是反转后的尾节点，相当于刚开始的dummy头，cur也需要重制

        return dummy_h.next
