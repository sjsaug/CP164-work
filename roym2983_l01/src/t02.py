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

from Food import Food

foodie = Food("Banana", 3, True, 140)
foodie2 = Food("Parfait", 6, True, 220)
foodie3 = Food("Orange Juice", 1, True, 175)

items = str(foodie)
items2 = str(foodie2)
items3 = str(foodie3)

print(f"""
{items}

{items2}

{items3}
""")
