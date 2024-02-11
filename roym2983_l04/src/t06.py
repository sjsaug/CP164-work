"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from src.List_array import *
from utilities import *
# Constants

lst = List()

src = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

array_to_list(lst, src)
print(f"Post array to list : {[i for i in lst]}")

target = []
list_to_array(lst, target)
print(f"Post list to array : {target}")
