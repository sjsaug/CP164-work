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
lst.append("four")
lst.append("five")

val = "two"
find = lst.find(val)
print(f"Found value '{find}' in list matching given value to find '{val}'")
val = "three"
index = lst.index(val)
print(f"Found {val} at index : {index}")
val = "test"
contains = val in lst
print(f"Is {val} in the list : {contains}")
