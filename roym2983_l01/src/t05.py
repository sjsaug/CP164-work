"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports

# Constants

from Food_utilities import read_foods

fh = open("foods.txt", "r")

items = read_foods(fh)

for each in items:
    print(each)
    print()
