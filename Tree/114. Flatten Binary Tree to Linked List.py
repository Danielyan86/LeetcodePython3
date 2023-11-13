# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # put the binary tree into a list
        pre_list = []

        def dsf(root):
            if root:
                pre_list.append(root)
                dsf(root.left)
                dsf(root.right)

        dsf(root)
        # use list to construct the new binary tree
        for i in range(1, len(pre_list)):
            pre, cur = pre_list[i - 1], pre_list[i]
            pre.left = None
            pre.right = cur
