# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def get_median(left, right):
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def buildTree(left, right):
            # return None if the two pointer are equal
            if left == right:
                return None

            mid = get_median(left, right)
            root = TreeNode(mid.val)
            # there is no need to find the left boundary, use dealing the condition in get_median method
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root

        # initial right boundary is None
        return buildTree(head, None)
