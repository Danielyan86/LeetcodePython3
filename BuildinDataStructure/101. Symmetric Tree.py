# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 看图，注意搞清楚节点入参位置
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if left is None and right is None:
                return True
            if left is None and right is not None:
                return False
            if left is not None and right is None:
                return False
            if left.val == right.val:
                return dfs(left.left, right.right) and dfs(left.right, right.left)
            else:
                return False

        if root is None:
            return True
        return dfs(root.left, root.right)
