class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 此方法最让人疑惑地方是最大和最小区间设定，左节点的左节点和右节点的右节点很好判断，
    # 只用判断比父节点小或者比父节点大，
    # 难点在于在于如果父节点是一个左节点，那么右节点除了大于父节点这个条件以外，还应该小于爷爷和爷爷往上节点
    # 乍一看，比较麻烦，还与需要维护一个列表，但是其实根据二叉搜索树性质，这种情况只需要大于父节点而小于爷爷就行了
    def isValidBST(self, root: TreeNode) -> bool:
        return self.valid(root, float("inf"), float("inf"))

    def valid(self, root, min_val, max_val):
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False

        return self.valid(root.left, min_val, root.val) and self.valid(root.right, root.val, max_val)
