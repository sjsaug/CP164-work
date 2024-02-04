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
var = 'test'
lst = List()

lst.append(1)
lst.append(2)
lst.append(3)
print(f"Post append : {[i for i in lst]}") 

lst.insert(0, var)
print(f"Post insert of {var} : {[i for i in lst]}") 

lst.remove('test')
print(f"Post removal of {var} : {[i for i in lst]}") 