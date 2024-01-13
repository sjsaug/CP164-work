"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Your Name
ID:      Your ID
Email:   your email@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports

# Constants

from Food_utilities import write_foods, get_food

fh = open("foods.txt", "a", encoding="utf-8")


foods = []

foods.append(get_food())

foods.append(get_food())

foods.append(get_food())

write_foods(fh, foods)
