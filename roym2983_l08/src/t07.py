"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# Imports

# Constants
'''The most inefficient tree would be one where the tree is heavily skewed to one side, essentially forming a linked list. This happens when the data is inserted in sorted order. The reason this is inefficient is because the time complexity of searching for a node in such a tree is O(n), where n is the number of nnodes.

The most efficient tree would be a perfectly balanced tree, where the left and right subtrees of every node differ in height by at most one. This minimizes the maximum number of comparisons needed to find an element in the tree, resulting in a time complexity of O(log n).

To theoretically figure out which tree is the most efficient, you could calculate the balance factor of each node in the tree (the height of the left subtree minus the height of the right subtree). A perfectly balanced tree would have a balance factor of 0, -1, or 1 for all nodes. The tree with the most nodes meeting this criteria would likely be the most efficient.'''