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
lst.prepend("start")
lst.append("end")
lst.insert(1, "middle")

for j in lst:
    print(j)
