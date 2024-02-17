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
lst.append("five")
lst.append("four")
lst.append("three")
lst.append("two")
lst.append("one")
peek = lst.peek()
print(f"First item in list : {peek}")
val = "one"
remove = lst.remove(val)
print(f"Removed value '{remove}' in list matching given value to remove '{val}'")
