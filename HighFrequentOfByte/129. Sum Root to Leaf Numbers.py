# 注意规律，从上往下是刚好满足十进制数字从高到底，所以乘以10是关键

# 起始参数传入0
# 否则返回左边加上右边的和值


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root, num):
            if root is None:
                return
            num = num * 10 + root.val
            dfs(root.left, num)
            dfs(root.right, num)
            if root.left is None and root.right is None:
                self.res += num

        dfs(root, 0)
        return self.res
