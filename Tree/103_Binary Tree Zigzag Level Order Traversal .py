# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        final_nums, node_queue = [], collections.deque()
        node_queue.append(root)
        while node_queue:
            num_tmp=[]
            for _ in range(len(node_queue)):
                node=node_queue.popleft()
                num_tmp.append(node.val)
                if node.left: node_queue.append(node.left)
                if node.right: node_queue.append(node.right)
            final_nums.append(num_tmp)
            if not node_queue: break
            num_tmp=[]
            for _ in range(len(node_queue)):
                node=node_queue.pop()
                num_tmp.append(node.val)
                if node.right: node_queue.appendleft(node.right)
                if node.left: node_queue.appendleft(node.left)
            final_nums.append(num_tmp)
        return final_nums