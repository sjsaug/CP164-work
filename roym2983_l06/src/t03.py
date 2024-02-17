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
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(1)

val = 1
count = lst.count(val)
print(f"Amount of times {val} is in list : {count} times")
max = lst.max()
print(f"Max value in list : {max}")
min = lst.min()
print(f"Min value in lsist : {min}")
