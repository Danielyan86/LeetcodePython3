# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        node_list = []
        node_list.append(root)
        min_deepth = 0
        while node_list:
            next_l_list = []
            min_deepth = min_deepth + 1
            for _ in range(len(node_list)):
                node = node_list.pop()
                if node.left is None and node.right is None:
                    next_l_list = []
                    break
                if node.left:
                    next_l_list.append(node.left)
                if node.right:
                    next_l_list.append(node.right)
            node_list = next_l_list
        return min_deepth
