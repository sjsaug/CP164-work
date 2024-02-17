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

prev, curr, index = lst._linear_search(3)

print(f"Prev : {prev._value}")
print(f"Curr : {curr._value}")
print(f"Index : {index}")
