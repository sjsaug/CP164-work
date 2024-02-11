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
# Constants

lst = List()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)
lst.append(6)
lst.append(7)
lst.append(8)
lst.append(9)
lst.append(10)

index = 0
getitem = lst[index]
print(f"Got item at index {index} : {getitem}")

lst[index] = 100
print(f"Set item at index {index} to : {lst[index]}")