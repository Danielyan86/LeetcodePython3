# 分治思想，归并排序，先归类，也就是分成最小两个元素后，再开始合并有序列表


# 需要特别注意的是，快慢指针法中的快指针起始位置要先走一步
# 否则只有两个节点时候就会出问题，慢指针将指向第二个节点，进入无限递归


# 合并两个有序链表参考这个 Merge k Sorted Lists https://leetcode.cn/problems/merge-k-sorted-lists/description/
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur2_h = slow.next
        slow.next = None  #  断开链表
        cur1, cur2 = self.sortList(head), self.sortList(cur2_h)

        # 合并链表
        cur = dummy = ListNode(0)
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        cur.next = cur1 if cur1 else cur2
        return dummy.next
