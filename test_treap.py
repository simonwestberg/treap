import treap


def _check_size(node, size=0):
    """Recursive function, visits all nodes and counts number of elements. Return
    the number of elements."""

    if node is None:
        return size
    else:
        size += 1
        size = _check_size(node.left_node, size)    # Go down the left tree
        size = _check_size(node.right_node, size)   # Go down the right tree
    return size


def check_size(tree):
    """Return the number of elements in treap."""

    return _check_size(tree.root)


def check_prio_and_sorted(node):
    """Check that a treap object fulfills the priority requirement and that its sorted correctly."""

    if node is None:
        return None    # The root is empty
    else:
        if (node.left_node is None) and (node.right_node is None):    # No children to compare with
            pass    # Do nothing
        elif node.left_node is None:    # No left child
            assert node.prio <= node.right_node.prio    # Check priority of right child and node
            assert node.data < node.right_node.data    # Check sorting
        elif node.right_node is None:    # No right child
            assert node.prio <= node.left_node.prio    # Check priority of left child and node
            assert node.data > node.left_node.data    # Check sorting
        else:    # Two children
            assert node.prio <= (node.left_node.prio and node.right_node.prio)    # Check priority of both left and right child with node
            assert (node.data > node.left_node.data) and (node.data < node.right_node.data)   # Check sorting
        check_prio_and_sorted(node.left_node)    # Recursion. Goes down the left tree first
        check_prio_and_sorted(node.right_node)    # Recursion. Goes down the right tree next


def test_delete():
    """Test the delete method in the Treap class."""

    tree = treap.Treap()
    tree.insert(5)
    assert not tree.delete(2)
    assert tree.delete(5)
    healthy(tree, [])

    tree.insert("hej")
    tree.insert("då")
    tree.insert("b")
    healthy(tree, ["b", "då", "hej"])
    tree.delete("hej")
    healthy(tree, ["b", "då"])
    tree.delete("b")
    healthy(tree, ["då"])
    tree.delete("då")
    healthy(tree, [])

    test = [5, 1, -3, 7, -3.3, 0, 17, 25, 3, 2, -7, 100, 24, 32, 11]
    temp = [5, 1, -3, 7, -3.3, 0, 17, 25, 3, 2, -7, 100, 24, 32, 11]
    for num in test:
        tree.insert(num)
    for num in test:
        assert tree.max() == max(temp)
        assert tree.min() == min(temp)
        assert tree.sorted_list() == sorted(temp)
        tree.delete(num)
        temp.remove(num)
        healthy(tree)
    assert tree.max() is None
    assert tree.min() is None
    healthy(tree, [])


def test_sort():
    """Test the sort function in the treap module."""

    test = [3, 2, 1]
    assert treap.sort(test) == [1, 2, 3]
    test = [5, 8, -4, 77.5, 0, 3, -3]
    assert treap.sort(test) == sorted(test)
    test = ["Du", "Bb", "Ge", "Att", "Ett", "Besk", "C", "Hej"]
    assert treap.sort(test) == ["Att", "Bb", "Besk", "C", "Du", "Ett", "Ge", "Hej"]


def healthy(tree, lis=None):
    """Checks that the treap is healthy. Tests the size() method.
    Checks that the treap fulfills the priority requirement and
    that it's sorted correctly. If the (correct) list is passed,
    the function checks that the method sorted_list() returns the
    correct list.
    """

    assert tree.size() == check_size(tree)

    if tree.size() == 0:  # Treap is empty
        assert tree.root is None
    if tree.size() == 1:  # Treap contains one element
        assert tree.root is not None
        assert tree.root.left_node is None
        assert tree.root.right_node is None

    if lis is None:
        pass    # Do nothing
    else:
        assert tree.sorted_list() == lis

    check_prio_and_sorted(tree.root)


def main_test():
    """Test the treap class."""

    test_delete()

    test_sort()

    tree = treap.Treap()   # Create empty tree. lis=[]
    assert tree.min() is None
    assert tree.max() is None
    assert not tree.search("Test")
    healthy(tree, [])

    tree.insert("Test")    # Insert one element. lis=["Test"]
    assert tree.min() == "Test"
    assert tree.max() == "Test"
    assert tree.search("Test")
    healthy(tree, ["Test"])

    tree.clear()    # Tree is now empty. lis=[]
    assert tree.min() is None
    assert tree.max() is None
    assert not tree.search("Test")
    healthy(tree, [])

    test = ("Du", "Bb", "Ge", "Att", "Ett", "Besk", "C", "Hej")
    for char in test:    # Insert different strings
        tree.insert(char)
    assert tree.search("Besk")
    assert tree.search("Bb")
    assert not tree.search("D")
    assert tree.min() == "Att"
    assert tree.max() == "Hej"
    healthy(tree, ["Att", "Bb", "Besk", "C", "Du", "Ett", "Ge", "Hej"])

    tree.clear()    # Tree is now empty
    test = (15.5, 11, 13, -12.2, 14, 10, 5.5, 8, 7, 6.6, 9, 4, -3, 2, 1)
    for num in test:
        tree.insert(num)
    assert tree.search(5.5)
    assert tree.search(9)
    assert not tree.search(1.1)
    assert tree.min() == -12.2
    assert tree.max() == 15.5
    healthy(tree, [-12.2, -3, 1, 2, 4, 5.5, 6.6, 7, 8, 9, 10, 11, 13, 14, 15.5])


for i in range(100):
    main_test()

