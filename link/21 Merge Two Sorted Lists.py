# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        else:
            # 代码可以再简化
            p1, p2 = list1, list2
            head, p3 = None, None
            if p1.val <= p2.val:
                head = p3 = p1
                p1 = p1.next
            else:
                head = p3 = p2
                p2 = p2.next
            p3.next = None
            while p1 and p2:
                if p1.val <= p2.val:
                    p3.next = p1
                    p1 = p1.next
                else:
                    p3.next = p2
                    p2 = p2.next
                p3 = p3.next
        # 注意最后一个边界条件
        p3.next = p1 if p1 else p2
        return head
