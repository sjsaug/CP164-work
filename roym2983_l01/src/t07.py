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

from Food_utilities import get_vegetarian, read_foods
from Food import Food

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

veggies = get_vegetarian(foods)

for each in veggies:
    print(each)
    print()
