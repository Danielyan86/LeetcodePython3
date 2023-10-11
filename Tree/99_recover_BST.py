class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.pre = TreeNode(float("-inf"))
        self.x, self.y = None, None
        self.helper(root)
        self.x.val, self.y.val = self.y.val, self.x.val

    def helper(self, node):
        if node is None:
            return
        self.helper(node.left)
        if node.val < self.pre.val:
            if self.x is None:
                self.x = self.pre
            self.y = node
        self.pre = node
        self.helper(node.right)


if __name__ == "__main__":
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    s = Solution()
    s.recoverTree(root)
    # print(s.root)
