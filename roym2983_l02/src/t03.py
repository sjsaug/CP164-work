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
from utilities import stack_to_array
# Constants

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
target = []
stack_to_array(stack, target)
print(f"Target List/Array : {target}")
print(f"Stack Empty Post Push : {Stack().is_empty()}")