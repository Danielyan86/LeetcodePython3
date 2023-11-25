class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 这题很有意思是用所谓的queue数据结构，结果运行效率更慢
import queue


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res_list = []
        node_queue = queue.Queue()
        if root:
            node_queue.put(root)
        else:
            return []
        while not node_queue.empty():
            res = []
            for _ in range(node_queue.qsize()):
                node = node_queue.get()
                res.append(node.val)
                if node.left:
                    node_queue.put(node.left)
                if node.right:
                    node_queue.put(node.right)
            res_list.append(res)
        return

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res_list, node_list = [], []
        if root:
            node_list.append(root)
        else:
            return []
        while node_list:
            res_level, node_tmp_l = [], []

            for node in node_list:
                res_level.append(node.val)
                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)
            node_list = node_tmp_l
            res_list.append(res_level)
        return res_list
