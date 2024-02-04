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
from List_array import *
# Constants
index_val = 4
find_val = 3
contain_val = 5
count_val = 2

lst = List()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)

max = lst.max()
print(f"Max value : {max}")

min = lst.min()
print(f"Min value : {min}")

index = lst.index(index_val)
print(f"Test of index({index_val}) : {index}")

find = lst.find(find_val)
print(f"Test of find({find_val}): {find}")

contains = contain_val in lst
print(f"List contains {contain_val} : {contains}")

count = lst.count(count_val)
print(f"Test of count({count_val}): {count}")
