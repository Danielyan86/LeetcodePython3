# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return head
        node_list = []
        cur = head
        while cur:
            node_list.append(cur)
            cur = cur.next

        i, j = 0, len(node_list) - 1
        if j == 1:
            return head
        while i < j:
            # 需要注意要一个一个连接，不能一起链接
            node_list[i].next = node_list[j]
            i += 1
            if i == j:
                break
            node_list[j].next = node_list[i]
            j -= 1

        node_list[i].next = None
