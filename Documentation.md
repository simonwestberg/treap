# treap module 1.0.0

Treap data structure to store either strings or numbers (ints and floats).

A treap (tree+heap) is a randomized binary search tree. It combines the sorted order of a binary search tree and the min heap property of a heap. It attempts to keep the tree balanced with rotations according to random priority numbers (min heap).

A binary search tree is a binary tree structure consisting of nodes. Each node m contains a value from a well-ordered set. Every node in the left sub-tree of m has a value thats less than the value of m, and every node in the right sub-tree has a value thats greater than the value of m. The min heap property of the treap says that a parent-node's priority number must be smaller than or equal to its children's priority numbers.

The average time complexity for most operations is O(log(n)) since an element is never more than about log2(n) steps away, where n is the number of elements.

***

The module defines the following **types**:

*class* treap.**Treap**()

*Create empty treap*

***

The module defines the following **methods**:

treap.**insert**(data)

*Insert the data in the treap. Can insert either strings or numbers, not both. Can't insert two identical elements.*

treap.**delete**(data)

*Remove the data from the treap and return True. Return False if the data is not in the treap.*

treap.**size**()

*Return the number of elements in the treap.*

treap.**search**(data)

*Return True if the data is in the treap, False if it's not.*

treap.**clear**()

*Remove all elements from the treap.*

treap.**sorted_list**()

*Return a sorted list of all the elements in the treap.*

treap.**min**()

*Return the smallest element in the treap. Return None if the treap is empty.*

treap.**max**()

*Return the largest element in the treap. Return None if the treap is empty.*

***

The module defines the following **functions**:

treap.**sort**(sequence)

*Sort a sequence of either strings or numbers (floats and ints). Return the elements in a sorted list.*




















