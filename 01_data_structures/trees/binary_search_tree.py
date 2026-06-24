class TreeNode:
    """
    This is just a single room (or node) in the tree.
    It holds a number and has two arms: one pointing left for smaller numbers,
    and one pointing right for bigger numbers.
    """

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    This is the main tree manager.
    The tree itself doesn't hold all the data; it just remembers where the
    front door (the root) is. We use recursion to find everything else.
    """

    def __init__(self):
        # A brand new tree always starts completely empty.
        self.root = None

    # =========================================================================
    # INSERTION: Adding elements
    # =========================================================================
    def insert(self, value):
        """The public method anyone can call to drop a number into the tree."""
        if self.root is None:
            # If the tree is totally empty, this new number gets to be the root!
            self.root = TreeNode(value)
        else:
            # Otherwise, hand it off to the helper to find where it belongs.
            self._insert_helper(self.root, value)

    def _insert_helper(self, current_node, value):
        """The recursive worker that actually walks down the tree to insert."""
        if value < current_node.val:
            # If the number is smaller, we have to look down the left branch.
            if current_node.left is None:
                # Found an empty slot! Hook up the new node here.
                current_node.left = TreeNode(value)
            else:
                # Someone is already here, so keep digging down the left side.
                self._insert_helper(current_node.left, value)
        else:
            # If the number is bigger or equal, we look down the right branch.
            if current_node.right is None:
                # Found an empty slot! Hook up the new node here.
                current_node.right = TreeNode(value)
            else:
                # Someone is already here, so keep digging down the right side.
                self._insert_helper(current_node.right, value)

    # =========================================================================
    # SEARCH: Finding elements
    # =========================================================================
    def search(self, value):
        """The clean public method to check if a number is inside the tree."""
        if self.root is None:
            return False
        return self._search_helper(self.root, value)

    def _search_helper(self, current_node, value):
        """The recursive finder that cuts the tree in half with every step."""
        # Case 1: We hit a dead end (None), meaning the number isn't in the tree.
        if current_node is None:
            return False

        # Case 2: Bingo! We found the exact room holding our number.
        if current_node.val == value:
            return True

        # Case 3: If we haven't found it yet, use the BST rules to pick a direction.
        if value < current_node.val:
            # The target is smaller, so ignore the right side and search left.
            return self._search_helper(current_node.left, value)
        else:
            # The target is bigger, so ignore the left side and search right.
            return self._search_helper(current_node.right, value)

    # =========================================================================
    # IN-ORDER TRAVERSAL: Left -> Parent -> Right
    # =========================================================================
    def in_order(self):
        """Public manager to print the tree from smallest to largest."""
        if self.root is None:
            return
        self._in_order_helper(self.root)
        print()  # Drop to a clean new line in the terminal when finished.

    def _in_order_helper(self, current_node):
        """
        My plan here is to exhaust the absolute smallest numbers first.
        By waiting to print the parent until the left side finishes,
        the output automatically comes out perfectly sorted.
        """
        if current_node is not None:
            self._in_order_helper(current_node.left)  # 1. Check everything smaller first.
            print(current_node.val, end=" ")  # 2. Print the current parent number.
            self._in_order_helper(current_node.right)  # 3. Check everything bigger next.

    # =========================================================================
    # PRE-ORDER TRAVERSAL: Parent -> Left -> Right
    # =========================================================================
    def pre_order(self):
        """Public manager to print parents before checking their children."""
        if self.root is None:
            return
        self._pre_order_helper(self.root)
        print()

    def _pre_order_helper(self, current_node):
        """
        My plan here is to log the parent node immediately before diving down.
        This is perfect if I ever want to copy or clone this exact tree layout.
        """
        if current_node is not None:
            print(current_node.val, end=" ")  # 1. Print the parent first!
            self._pre_order_helper(current_node.left)  # 2. Now go check the left branch.
            self._pre_order_helper(current_node.right)  # 3. Finally, check the right branch.

    # =========================================================================
    # POST-ORDER TRAVERSAL: Left -> Right -> Parent
    # =========================================================================
    def post_order(self):
        """Public manager to print all the children before their parents."""
        if self.root is None:
            return
        self._post_order_helper(self.root)
        print()

    def _post_order_helper(self, current_node):
        """
        My plan here is to delay printing the parent until its children are done.
        This is exactly how I would delete a tree, since I'd need to clear out
        the children before destroying the parent that points to them.
        """
        if current_node is not None:
            self._post_order_helper(current_node.left)  # 1. Clear out the left child side.
            self._post_order_helper(current_node.right)  # 2. Clear out the right child side.
            print(current_node.val, end=" ")  # 3. Print the parent last.


# =========================================================================
# 🧪 RUNNING TESTS
# =========================================================================

tree = BinarySearchTree()

# Populating the tree structure
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

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

print("----------------------------\n")

print("--- Search Tests ---")
print("Searching for 30: ", tree.search(30))  # True
print("Searching for 70: ", tree.search(70))  # True
print("Searching for 99: ", tree.search(99))  # False
print("----------------------------\n")

print("--- Manual Pointer Checks ---")
print("Root Node:           ", tree.root.val)
print("Left of Root:        ", tree.root.left.val)
print("Right of Root:       ", tree.root.right.val)
print("Far Left (20 Node):  ", tree.root.left.left.val)
print("----------------------------")