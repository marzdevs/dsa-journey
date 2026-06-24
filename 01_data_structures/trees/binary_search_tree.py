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

    def search(self, value):
        if self.root is None:
            return False
        else:
           return self._search_helper(self.root, value)

    def _search_helper(self, current_node, value):
        if current_node is None:
            return False
        if current_node.val == value:
            return True
        if value < current_node.val:
            return self._search_helper(current_node.left, value)
        else:
            return self._search_helper(current_node.right, value)
    # Tree Traversals
    def in_order(self):
        if self.root is None:
            return
        else:
            self._in_order_helper(self.root)
            print()

    def _in_order_helper(self, current_node):
        if current_node is not None:
            # 1. Tell a clone to go all the way left
            self._in_order_helper(current_node.left)

            # 2. Print the current room's value
            print(current_node.val, end=" ")

            # 3. Tell a clone to go all the way right
            self._in_order_helper(current_node.right)

    def pre_order(self):
        if self.root is None:
            return
        else:
            self._pre_order_helper(self.root)
            print()

    def _pre_order_helper(self, current_node):
        if current_node is not None:
            print(current_node.val, end=" ")
            self._pre_order_helper(current_node.left)
            self._pre_order_helper(current_node.right)

    def post_order(self):
        if self.root is None:
            return
        else:
            self._post_order_helper(self.root)
            print()

    def _post_order_helper(self, current_node):
        if current_node is not None:
            self._post_order_helper(current_node.left)
            self._post_order_helper(current_node.right)
            print(current_node.val, end=" ")




# Initialize your tree
tree = BinarySearchTree()

# Build the structure
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

# Run and compare all three traversals!
print("--- Tree Traversal Tests ---")

print("1. In-Order (Left -> Parent -> Right):")
print("   Expected: 20 30 40 50 60 70 80")
print("   Actual:   ", end="")
tree.in_order()

print("\n2. Pre-Order (Parent -> Left -> Right):")
print("   Expected: 50 30 20 40 70 60 80")
print("   Actual:   ", end="")
tree.pre_order()

print("\n3. Post-Order (Left -> Right -> Parent):")
print("   Expected: 20 40 30 60 80 70 50")
print("   Actual:   ", end="")
tree.post_order()

print("----------------------------")

print(tree.search(30))  # Should print: True
print(tree.search(70))  # Should print: True
print(tree.search(99))  # Should print: False (it ran off the edge!)

# Print values directly by following your pointer paths
print("Root:", tree.root.val)          # Should be 50
print("Left:", tree.root.left.val)     # Should be 30
print("Right:", tree.root.right.val)   # Should be 70
print("Far Left of:", tree.root.left.left.val) # Should be 20