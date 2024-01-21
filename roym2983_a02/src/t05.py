"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-01-21"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from Food_utilities import food_search
# Constants

fh = open('foods.txt', 'r', encoding='utf-8')
foods = read_foods(fh)

food_search = food_search(foods, 0, 1000, False)
for food in food_search:
    print(food)
