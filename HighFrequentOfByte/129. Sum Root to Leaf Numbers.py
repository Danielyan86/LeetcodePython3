# 注意规律，从上往下是刚好满足十进制数字从高到底，所以乘以10是关键
# 如果左右都是返回0，也就是没有左右子节点时候，返回当前已经求和的数字值，因为从上往下，表示走到头了
# 否则返回左边加上右边的和值
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num):
            if node is None:
                return 0
            num = num * 10 + node.val
            l = dfs(node.left, num)
            r = dfs(node.right, num)
            return num if l == 0 and r == 0 else l + r

        return dfs(root, 0)
