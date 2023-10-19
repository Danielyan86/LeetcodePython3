# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        if n == 0:
            return []
        self.p = postorder
        self.i = inorder
        return self.buildTree_helper(0, n - 1)

    def buildTree_helper(self, left, right):
        if left > right:
            return None
        val = self.p.pop()
        root = TreeNode(val)

        index = self.i.index(val)
        root.right = self.buildTree_helper(index + 1, right)
        root.left = self.buildTree_helper(left, index - 1)
        return root
