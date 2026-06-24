class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        # When a brand new tree is created, it starts completely empty
        self.root = None

    def insert(self, value):
        # Your code goes here
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_helper(self.root, value)

    def _insert_helper(self, current_node, value):
        if value < current_node.val:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_helper(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_helper(current_node.right, value)


# Initialize your tree
tree = BinarySearchTree()

# Build the structure
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)

# Print values directly by following your pointer paths
print("Root:", tree.root.val)          # Should be 50
print("Left:", tree.root.left.val)     # Should be 30
print("Right:", tree.root.right.val)   # Should be 70
print("Far Left of:", tree.root.left.left.val) # Should be 20