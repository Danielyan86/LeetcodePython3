# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums = nums
        return self.helper(0, len(nums) - 1)

    def helper(self, left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        root = TreeNode(self.nums[mid])

        root.left = self.helper(left, mid - 1)
        root.right = self.helper(mid + 1, right)
        return root
