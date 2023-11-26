# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        node_s = set()
        cur = head
        while cur:
            if cur in node_s:
                return cur
            node_s.add(cur)
            cur = cur.next


class Solution2:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        if head.next is head:
            return head
        slow, fast = head, head

        while True:
            if fast is None or fast.next is None:
                return
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break

        fast = head  # set the fast pointer from start position
        # the fast need to move 1 step for second time
        while fast:
            if slow == fast:
                return slow
            slow, fast = slow.next, fast.next
