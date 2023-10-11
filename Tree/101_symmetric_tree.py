class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.helper_dfs(root.left, root.right)

    def helper_dfs(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:  # 需要注意不相等时候提前中断搜索，而不是相等
            return False
        return self.helper_dfs(left.left, right.right) and self.helper_dfs(
            left.right, right.left
        )
