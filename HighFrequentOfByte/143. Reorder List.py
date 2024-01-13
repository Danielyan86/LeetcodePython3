class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 快慢指针大法找到链表中点
        if head.next is None:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre, cur = None, slow.next
        slow.next = None
        # 反转后半段链表
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        # 合并两个链表
        cura, curb = head, pre
        while curb:
            tmpa, tmpb = cura.next, curb.next
            cura.next = curb
            curb.next = tmpa
            cura, curb = tmpa, tmpb
            # curb=tmpb
        # return head
