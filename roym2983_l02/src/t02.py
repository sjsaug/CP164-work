"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack
# Constants

stack = Stack()

main = [1, 2, 3, 4, 5]
print(f"Main : {main}")
array_to_stack(stack, main)
print(f"Main After : {main}")

for element in stack:
    print(f"Elem : {element}")