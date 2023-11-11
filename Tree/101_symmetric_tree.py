class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.helper_dfs(root.left, root.right)

    def helper_dfs(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:  # 需要注意不相等时候提前中断搜索，而不是相等
            return False
        return self.helper_dfs(left.left, right.right) and self.helper_dfs(
            left.right, right.left
        )


class Solution2:
    # use queue to implement
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or not (root.left or root.right):
            return True
        # 用队列保存节点
        queue = [root.left, root.right]
        while queue:
            # 从队列中取出两个节点，再比较这两个节点
            left = queue.pop(0)
            right = queue.pop(0)
            # 如果两个节点都为空就继续循环，两者有一个为空就返回false
            if not (left or right):
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            # 将左节点的左孩子， 右节点的右孩子放入队列
            queue.append(left.left)
            queue.append(right.right)
            # 将左节点的右孩子，右节点的左孩子放入队列
            queue.append(left.right)
            queue.append(right.left)
        return True
