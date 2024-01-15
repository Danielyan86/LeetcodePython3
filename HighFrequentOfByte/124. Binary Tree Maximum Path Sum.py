# 和236. Lowest Common Ancestor of a Binary Tree 类似
# 后续遍历模版


# 设置一个全局的max变量，注意每次max的值
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def dfs(node):
            if node is None:
                return 0
            nonlocal max_sum
            # Calculate the maximum path sum in the left and right subtrees
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Update the maximum path sum
            max_sum = max(max_sum, left + right + node.val)

            # Return the maximum path sum that can be extended from the current node
            return max(left, right) + node.val

        # max_sum = float('-inf')  # Initialize max_sum to negative infinity
        dfs(root)

        return max_sum
