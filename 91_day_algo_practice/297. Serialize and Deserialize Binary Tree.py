class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""

        def helper(node):
            if node is None: return "None"
            return "".join((str(node.val) + "," + helper(node.left) + "," + helper(node.right)))

        return helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""

        def helper(data_list):
            if data_list[0] == "None":
                data_list.popleft()
                return None
            # if string is not None, construct the node
            root = TreeNode(int(data_list[0]))
            data_list.popleft()
            root.left = helper(data_list)
            root.right = helper(data_list)
            return root

        # use deque to improve the efficiency of poping the first item of list
        data_list = collections.deque(data.split(","))
        return helper(data_list)


# Example usage:
# Constructing a sample tree:  1
#                            /   \
#                           2     3
#                               /   \
#                              4     5

if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.right.left = TreeNode(4)
    tree.right.right = TreeNode(5)

    # Serialize the tree
    codec = Codec()
    serialized_tree = codec.serialize(tree)
    print("Serialized Tree:", serialized_tree)

    # Deserialize the tree
    deserialized_tree = codec.deserialize(serialized_tree)
    print("Deserialized Tree:", deserialized_tree)
