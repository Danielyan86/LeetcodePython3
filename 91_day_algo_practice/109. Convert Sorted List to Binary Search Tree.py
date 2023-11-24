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
        # get the value of middle node
        def get_middle(left, right):
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def build_tree(left, right):
            if left == right:
                return None
            mid = get_middle(left, right)
            root = TreeNode(mid.val)  # build root node
            root.left = build_tree(left, mid)
            root.right = build_tree(mid.next, right)
            return root

        return build_tree(head, None)
