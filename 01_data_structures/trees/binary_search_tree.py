class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def insert(root, value):
        # Your code goes here
        if root is None:
            root = TreeNode(value)
            return root
        else:
            if value < root.val:
                # Pass the value down to the left child,
                # and capture whatever node it returns back into root.left
                root.left = insert(root.left, value)
            else:
                # Do the exact same thing for the right side
                root.right = insert(root.right, value)

            # CRITICAL STEP: Always return the root at the end of the else block
            return root