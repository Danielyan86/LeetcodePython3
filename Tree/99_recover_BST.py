# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node_list = []
        self.valid(root, float('inf'), float('inf'), node_list)
        print(node_list)
        node_list[0].val, node_list[1].val = node_list[1].val, node_list[0].val
        print(node_list)
        print(root)

    def valid(self, root, min_val, max_val, node_list=[]):
        if not root:
            return
        if root.left and root.val < root.left.val:
            node_list.append(root)
        if root.right and root.val > root.right.val:
            node_list.append(root)

        if root.val <= min_val or root.val >= max_val:
            print("lala", root)
            node_list.append(root)
            return

        self.valid(root.left, min_val, root.val)
        self.valid(root.right, root.val, max_val)


if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(3)
    right = TreeNode(2)
    root.left = left
    root.right = right
    s = Solution()
    s.recoverTree(root)
