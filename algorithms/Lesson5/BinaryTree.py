"""
Every node has some value, and pointers to left and right children.
You'll need to implement two methods:
search(): which searches for the presence of a node in the tree.
print_tree(): which prints out the values of tree nodes in a pre-order traversal.
You should attempt to use the helper methods provided to create recursive solutions to these functions.
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root, self.root.value)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        found = False
        if start.value == find_val:
            return True
        if start.left:
            found = self.preorder_search(start.left, find_val)
        if not found:
            if start.right:
                found = self.preorder_search(start.right, find_val)
        return found

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start.left:
            traversal = str(traversal) + "-%s" % self.preorder_print(start.left, start.left.value)
        if start.right:
            traversal = str(traversal) + "-%s" % self.preorder_print(start.right, start.right.value)
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))


# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())
