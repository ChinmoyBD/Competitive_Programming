class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
	    self.root = TreeNode(val)
	else:
	    
