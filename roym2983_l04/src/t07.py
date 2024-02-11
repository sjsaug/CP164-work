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
from utilities import *
from Food_utilities import *
# Constants

lst = List()
fh = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fh)
for i in foods:
    lst.append(i)

list_test(lst)
