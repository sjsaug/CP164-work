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

'''The reason for having separate trees for encoding and decoding, even though they store the same combination of letters and codes, is due to the nature of binary search trees (BSTs).
In a BST, each node's key must be greater than all keys in its left subtree and less than all keys in its right subtree. This property allows us to efficiently search for a specific key in the tree.

When encoding, we're converting letters to Morse code, so we need to be able to quickly find a specific letter in the tree. Therefore, we use a BST where the keys are the letters.
When decoding, we're converting Morse code to letters, so we need to be able to quickly find a specific Morse code in the tree. Therefore, we use a BST where the keys are the Morse codes.

Even though the data (letters and codes) iss the same in both trees, the keys (which determine the structure of the tree) are different. That's why we need two separate trees.'''