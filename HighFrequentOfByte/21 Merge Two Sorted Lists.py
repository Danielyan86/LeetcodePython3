# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 注意cur指针的移动是独立的
# 前面none的判断不需要，后面覆盖了
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 is None: return list2
        # if list2 is None: return list1
        # if list1 is None and list2 is None: return
        cur = dummy_h = ListNode(0)
        cur1, cur2 = list1, list2
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
                # cur=cur1
            else:
                cur.next = cur2
                cur2 = cur2.next
                # cur=cur2
            cur = cur.next
        if cur1:
            cur.next = cur1
        if cur2:
            cur.next = cur2

        return dummy_h.next
