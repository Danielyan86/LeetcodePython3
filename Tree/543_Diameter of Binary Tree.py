# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 需要搞清楚最大直径怎么推导出来的，和节点数相关
        self.ans = 1

        def helper(root):
            if root is None:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.ans = max(self.ans, left + right + 1)
            # 每次经过一个节点，+1即可，不用想太复杂
            return max(left, right) + 1

        helper(root)
        return self.ans - 1
