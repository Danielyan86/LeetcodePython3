# 快慢指针找中点，指针断开，反转链表，插入第二个链表
# 注意链表一定要断开，不然会死循环！
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre, cur = None, slow.next
        slow.next = None  # 链表一定要断开
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        cur1, cur2 = head, pre
        while cur2:
            tmp1, tmp2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = tmp1
            cur1, cur2 = tmp1, tmp2
        return head
