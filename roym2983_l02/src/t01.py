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
# Constants

stack = Stack()

print(f"Stack Empty : {Stack().is_empty()}")
stack.push(10)
stack.push(20)
stack.push(30)
print(f"Stack Empty Post Push : {Stack().is_empty()}")
print(f"Stack Peek : {stack.peek()}")
print(f"Stack Pop : {stack.pop()}")
print(f"Stack Peek Post Pop : {stack.peek()}")

for element in stack:
    print(f"Elem : {element}")