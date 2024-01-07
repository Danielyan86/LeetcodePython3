# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 双指针实现
# 注意题目是除去所有重复元素，而不是把重复元素减少到一个，比如出现两个1，则一个1也不需要
# 核心在于找到重复元素的起点和终点，所以必须要有一个pre指针
# 如果没有出现重复元素，则两个指针永远相邻，注意利用这个特性
# 当cur和cur.next一样的时候，这个时候只需要移动cur指针
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy_h = ListNode(0, head)
        pre, cur = dummy_h, head
        while cur:
            if cur.next and cur.val == cur.next.val:
                cur = cur.next
            else:  # 剩下分两种情况，pre和cur已经不相邻，则说明已经出现过了重复元素
                if pre.next != cur:
                    pre.next = cur.next
                    cur = cur.next
                else:  # 否则直接把两个指针一起向前移动
                    pre, cur = pre.next, cur.next
        return dummy_h.next
