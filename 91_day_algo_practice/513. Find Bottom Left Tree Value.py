# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return
        queue = [root]  # use list to simulate the queue
        while queue:
            node = queue.pop(0)  # Pop the leftmost node in the current level
            if node.right:  # the right node should be append firstly
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            ans = node.val
        # The last node visited in the bottom row is the leftmost value
        return ans
