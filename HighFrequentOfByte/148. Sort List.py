# 分治思想，归并排序，先归类，也就是分成最小两个元素后，再开始合并有序列表
# 需要特别注意的是，快慢指针法快指针起始位置要先走一步
# 否则只有两个节点时候就会出问题，慢指针将指向第二个节点，进入无限递归
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        sp, fp = head, head.next  # 快慢指针法寻找link中点
        while fp and fp.next:
            sp, fp = sp.next, fp.next.next

        mid, sp.next = sp.next, None
        # recursive for cutting
        left, right = self.sortList(head), self.sortList(mid)

        # 合并两个有序链表
        # Merge k Sorted Lists https://leetcode.cn/problems/merge-k-sorted-lists/description/
        cur = dummy_h = ListNode(0)
        while left and right:
            if left.val < right.val:
                cur.next, left = left, left.next
            else:
                cur.next, right = right, right.next
            cur = cur.next

        cur.next = left if left else right
        return dummy_h.next
