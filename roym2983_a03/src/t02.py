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
from Stack_array import *
# Constants

stack1 = Stack()
stack2 = Stack()
target = Stack()
stack1.push(6)
stack2.push(5)
stack1.push(4)
stack2.push(3)
stack1.push(2)
stack2.push(1)
target.push(100)
target.push(200)
target.push(300)
target.combine(stack1, stack2)
print(target._values)
