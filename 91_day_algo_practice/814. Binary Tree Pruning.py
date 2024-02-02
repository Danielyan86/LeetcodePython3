class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 如果树的根节点为空，返回空
        if root is None:
            return

        # 递归地修剪左子树和右子树
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # 如果当前节点为叶子节点且值为0，则删除该节点
        if root.left is None and root.right is None and root.val == 0:
            return

        # 返回修剪后的树
        return root
