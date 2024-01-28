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
src = Stack()
src._values.extend([1, 2, 3])
print(f"Pre reverse source : {src._values}")
src.reverse()
print(f"Post reverse source : {src._values}")
