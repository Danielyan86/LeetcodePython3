# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # note use deep copy mehtod
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        res_l = []

        def helper(node, num_l):
            if node is None:
                return
            num_l.append(node.val)
            if node.left is None and node.right is None:
                if sum(num_l) == targetSum:
                    res_l.append(num_l)
                else:
                    del num_l
            else:
                helper(node.left, copy.deepcopy(num_l))
                helper(node.right, copy.deepcopy(num_l))

        helper(root, [])
        return res_l
