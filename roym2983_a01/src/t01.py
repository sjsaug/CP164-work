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
from functions import clean_list
# Constants

list = [23, 13, 21, 2, 4, 1, 4, 33, 66, 24]
print(f"Before : {list}")
clean_list(list)
print(f"After clean : {list}")
