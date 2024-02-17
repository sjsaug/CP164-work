"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports

# Constants

from List_linked import List
lst = List()
lst.append("one")
lst.append("two")
lst.append("three")
val = lst[1]
print(f"Prev value : {val}")
lst[1] = "test"
print(f"New value : {lst[1]}")
