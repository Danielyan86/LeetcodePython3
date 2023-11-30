class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node, num):
            if node is None: return 0
            num = num * 10 + node.val
            l = helper(node.left, num)
            r = helper(node.right, num)
            return num if not l and not r else l + r
        return helper(root, 0)

