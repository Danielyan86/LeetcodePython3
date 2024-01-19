# 和236. Lowest Common Ancestor of a Binary Tree 类似
# 后续遍历模版


# 设置一个全局的max变量，当max_sum 在函数内被作为参数使用时候，需要注意用nonlocal声明是全局变量
# 注意在左右节点返回计算结果时候，为什么为负数时候要取0？取0意义就是当前子节点返回值为负数，那么这样只会越加越小，不满足题目需求，起始也就是不用再去走当前子节点了。不用max函数更好理解一些
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def dfs(node):
            if node is None:
                return 0
            nonlocal max_sum
            # Calculate the maximum path sum in the left and right subtrees
            left = dfs(node.left)
            left = left if left >= 0 else 0
            right = dfs(node.right)
            right = right if right >= 0 else 0
            # Update the maximum path sum
            max_sum = max(max_sum, left + right + node.val)

            # Return the maximum path sum that can be extended from the current node
            return max(left, right) + node.val

        # max_sum = float('-inf')  # Initialize max_sum to negative infinity
        dfs(root)

        return max_sum
