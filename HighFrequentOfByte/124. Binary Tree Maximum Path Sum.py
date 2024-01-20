# 和 236. Lowest Common Ancestor of a Binary Tree 类似
# 后续遍历模版
# 但是不太一样的是max——sum是单独更新的，和return是分开的两句
#


# 设置一个全局的max变量，当max_sum 在函数内被作为参数使用时候，需要注意用nonlocal声明是全局变量
# 注意在左右节点返回计算结果时候，为什么为负数时候要取0？取0意义就是当前子节点返回值为负数，那么这样只会越加越小，不满足题目需求，起始也就是不用再去走当前子节点了.


# 为什么返回时候是取左边或者右边其中一个节点加上当前，而不是左右节点和？
# 左右节点加上当前这种情况已经在上一句计算过了
# 想象一下dfs路径，如果是左中右三种情况都遍历了，那么不可能再往上了，因此这是覆盖的第二种情况，


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_s = float("-inf")

        def dfs(root):
            if root is None:
                return 0
            nonlocal max_s
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            max_s = max(max_s, left + right + root.val)
            return max(left, right) + root.val

        dfs(root)
        return max_s
