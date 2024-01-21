# 看图 写code，注意搞清楚节点入参位置,
# 前面几种为None情况写全
# 如果值相等，则继续遍历，不能直接返回true
# 如果不想等，则直接返回False
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if left is None and right is None:
                return True
            if left is None and right:
                return False
            if left and right is None:
                return False
            if left.val == right.val:
                return dfs(left.left, right.right) and dfs(left.right, right.left)
            else:
                return False

        return dfs(root.left, root.right)
