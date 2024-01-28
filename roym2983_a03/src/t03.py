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
from functions import stack_reverse
from Stack_array import Stack
# Constants

src = Stack()
src.push(5)
src.push(3)
src.push(1)
print(f"Pre Reverse : {src}")
stack_reverse(src)
print(f"Post Reverse : {src}")
while not src.is_empty():
    print(src.pop())
