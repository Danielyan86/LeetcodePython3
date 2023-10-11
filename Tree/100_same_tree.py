class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False  # return the false directly, dont need further cursive
        left_res = self.isSameTree(p.left, q.left)
        right_res = self.isSameTree(p.right, q.right)
        return left_res and right_res


if __name__ == "__main__":
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    s = Solution()
    s.recoverTree(root)
    # print(s.root)
