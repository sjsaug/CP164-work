"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
# Imports
from functions import list_subtraction
# Constants

list = [23, 13, 21, 2, 4, 1, 4, 33, 66, 24]
print(f"Before : {list}")
list_subtraction(list, [1, 2, 3, 4, 5, 6])
print(f"After subtraction : {list}")