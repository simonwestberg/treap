"""
Treap data structure to store either strings or numbers (ints and floats).

A treap (tree+heap) is a randomized binary search tree. It combines the
sorted order of a binary search tree and the min heap property of a heap.
It attempts to keep the tree balanced with rotations according to random
priority numbers (min heap).

A binary search tree is a tree structure consisting of
nodes. Each node m contains a value from a well-ordered set.
Every node in the left sub-tree of m has a value thats less
than the value of m, and every node in the right
sub-tree has a value thats greater than the value of m.
The min heap property of the treap says that a parent-node's
priority number must be smaller than or equal to
its children's priority numbers.

The average time complexity for operations insert, delete
and search are O(log(n)) since an element is never more than
about log2(n) steps away, where n is the number of elements.
"""


import random


class _TreapNode:
    """
    Nodes to be used in the Treap class. A node contains
    some data from a well ordered set (either numbers or strings),
    a reference to the left and right sub-node, and a random
    priority number.
    """

    def __init__(self, data=None):
        """Constructor."""

        self.data = data
        self.left_node = None
        self.right_node = None
        self.prio = random.randint(0, 1000000)


def _left_rotation(tree):
    """
    Help function for Treap class. Rotates the tree counter-clockwise
    without changing the sorted order. Returns the rotated tree.
    Example:

       A              B
     /  \           /  \
         B   -->   A
       /  \      /  \

    A is tree (input argument) and B is new_tree (output).
    """

    new_tree = tree.right_node    # B
    tree.right_node = new_tree.left_node    # Change the necessary references
    new_tree.left_node = tree
    return new_tree


def _right_rotation(tree):
    """
    Help function for Treap class. Rotates the tree clockwise
    without changing the sorted order. Returns the rotated tree.
    Example:

         B            A
       /  \         /  \
      A       -->       B
    /  \              /  \

    B is tree (input argument) and A is new_tree (output).
    """

    new_tree = tree.left_node    # A
    tree.left_node = new_tree.right_node    # Change the necessary references
    new_tree.right_node = tree
    return new_tree


class Treap:
    """
    Randomized binary search tree. Attempts to keep the tree
    balanced with rotations according to min heap property.
    Can store either strings or numbers (ints and floats),
    not both. Can't contain two identical objects.
    """

    def __init__(self):
        """Constructor. Create empty treap."""

        self.root = None
        self._lis = []    # List to store sorted elements.
        self._size = 0    # Empty treap has size zero.

    def _insert(self, new_node, tree):
        """Insert new node in tree and return the updated tree."""

        if tree is None:    # The tree is empty
            return new_node

        if new_node.data == tree.data:
            raise ValueError("Treap can't contain two identical elements.")
        if isinstance(new_node.data, str):
            if not isinstance(tree.data, str):
                raise ValueError("Treap can't contain different data types.")
        else:
            if isinstance(tree.data, str):
                raise ValueError("Treap cant contain different data types.")

        if new_node.data < tree.data:
            tree.left_node = self._insert(new_node, tree.left_node)    # Insert the new node in the left sub-tree.
            if tree.prio > tree.left_node.prio:
                tree = _right_rotation(tree)    # Perform a right rotation in attempt to keep tree balanced.
        else:
            tree.right_node = self._insert(new_node, tree.right_node)    # Insert the new node in the right sub-tree.
            if tree.prio > tree.right_node.prio:
                tree = _left_rotation(tree)    # Perform a left rotation in attempt to keep tree balanced.
        return tree

    def insert(self, data):
        """Insert the data in the Treap. Can't insert two identical elements.
        Can insert either strings or numbers, not both.
        """

        new_node = _TreapNode(data)    # Create a new node containing the data and two None-pointers
        self.root = self._insert(new_node, self.root)    # Insert the new node at the root
        self._size += 1    # The tree size is increased by one

    def _inorder_traversal(self, root):
        """
        Visits all nodes in sorted order. Takes a root (node) as input.
        Returns a list with all elements in sorted order.
        """

        if root is None:
            return None    # The root is empty
        else:
            self._inorder_traversal(root.left_node)    # Goes down the left sub-tree first
            self._lis.append(root.data)    # Adds the nodes data to the list
            self._inorder_traversal(root.right_node)    # Goes down the right sub-tree next
        return self._lis

    def sorted_list(self):
        """Return a sorted list of all the elements in the treap."""

        if self.size() == 0:
            return []    # The tree is empty
        else:
            temp = self._inorder_traversal(self.root)    # Create sorted list
            self._lis = []    # The _lis variable is reset
            return temp

    def size(self):
        """Return the number of elements in the treap."""

        return self._size

    def clear(self):
        """Remove all elements from the treap."""

        self.root = None
        self._lis = []
        self._size = 0

    def _search(self, root, data):
        """Searches the tree recursively for the data. Returns
        True if the data is in the treap, False if it's not.
        """

        if root is None:
            return False
        elif root.data == data:
            return True
        elif data < root.data:
            return self._search(root.left_node, data)    # Search the left sub-tree
        else:
            return self._search(root.right_node, data)    # Search the right sub-tree

    def search(self, data):
        """Return True if the data is in the treap, False if it's not."""

        return self._search(self.root, data)    # Start the search at the root

    def _delete(self, root, data):
        """Delete the data from the treap."""

        if root.data == data:    # We have reached the node to be deleted
            if (root.left_node is None) and (root.right_node is None):    # No children, change the root to None
                root = None
            elif root.left_node is None:    # No left node, change the root to the roots right node
                root = root.right_node
            elif root.right_node is None:    # No right node, change the root to the roots left node
                root = root.left_node
            else:    # Root has two nodes
                if root.left_node.prio < root.right_node.prio:
                    root = _right_rotation(root)    # Move the node to be deleted one step "down", keep min heap order
                    root.right_node = self._delete(root.right_node, data)    # Recursive call
                else:
                    root = _left_rotation(root)    # Move the node to be deleted one step "down", keep min heap order
                    root.left_node = self._delete(root.left_node, data)    # Recursive call

        elif data < root.data:
            root.left_node = self._delete(root.left_node, data)    # Recursive call on left sub-tree
        else:
            root.right_node = self._delete(root.right_node, data)    # Recursive call on right sub-tree
        return root

    def delete(self, data):
        """Remove the data from the treap and return True. Return
        False if the data is not in the treap.
        """

        if self.search(data):    # The data is in the treap
            self.root = self._delete(self.root, data)
            self._size -= 1    # The treap size decreases by one
            return True
        else:
            return False

    def min(self):
        """Return the smallest element in the treap. Return None
        if the treap is empty.
        """

        if self.size() == 0:
            return None
        else:
            current = self.root
            while current.left_node is not None:    # Iterate through the left sub-nodes
                current = current.left_node
            return current.data

    def max(self):
        """Return the largest element in the treap. Return None
        if the treap is empty.
        """

        if self.size() == 0:
            return None
        else:
            current = self.root
            while current.right_node is not None:    # Iterate through the right sub-nodes
                current = current.right_node
            return current.data


def sort(lis):
    """Sort a sequence of either strings or
    numbers (floats and ints). Return the
    elements in a sorted list.
    """

    tree = Treap()
    for elem in lis:
        tree.insert(elem)
    return tree.sorted_list()

