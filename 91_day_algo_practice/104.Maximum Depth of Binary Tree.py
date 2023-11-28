class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.max_depth = 0
        depth = 0

        def helper(node, depth):
            if node is None:
                return
            depth += 1
            if node.left is None and node.right is None:
                self.max_depth = max(self.max_depth, depth)
            helper(node.left, depth)
            helper(node.right, depth)

        helper(root, depth)
        return self.max_depth


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 0
        deque = collections.deque([root])
        while deque:
            depth += 1
            for _ in range(len(deque)):
                node = deque.popleft()
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
        return depth
