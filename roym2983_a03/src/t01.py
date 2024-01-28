"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
# Imports
from functions import stack_combine
from Stack_array import Stack
# Constants
stack1 = Stack()
stack2 = Stack()

stack1.push(6)
stack2.push(5)
stack1.push(4)
stack2.push(3)
stack1.push(2)
stack2.push(1)

combined_stack = stack_combine(stack1, stack2)
for i in combined_stack:
    print(f" : {i}")
