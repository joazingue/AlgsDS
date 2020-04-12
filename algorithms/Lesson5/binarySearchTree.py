"""
This time, you'll implement search() and insert().
You should rewrite search() and not use your code from the last exercise so it takes advantage of BST properties.
Feel free to make any helper functions you feel like you need, including the print_tree() function from earlier for debugging.
You can assume that two nodes with the same value won't be inserted into the tree.
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root, self.root.value)

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start.left:
            traversal = str(traversal) + "-%s" % self.preorder_print(start.left, start.left.value)
        if start.right:
            traversal = str(traversal) + "-%s" % self.preorder_print(start.right, start.right.value)
        return traversal

    def insert(self, new_val):
        new_node = Node(new_val)
        self.root = self.bst_insert(self.root, new_node)

    def bst_insert(self, parent, new_node):
        if parent.value > new_node.value:
            if parent.left:
                parent.left = self.bst_insert(parent.left, new_node)
            else:
                parent.left = new_node
        else:
            if parent.right:
                parent.right = self.bst_insert(parent.right, new_node)
            else:
                parent.right = new_node
        return parent

    def search(self, find_val):
        return self.bst_search(self.root, find_val)

    def bst_search(self, node, val):
        found = False
        if node:
            if node.value == val:
                return True
            if val < node.value:
                found = self.bst_search(node.left, val)
            else:
                found = self.bst_search(node.right, val)
        return found


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print(tree.print_tree())

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
