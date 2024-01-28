"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
# Imports
from functions import postfix
# Constants

expression = "2 3 + 4 5 * -"
print(f'Infix : {expression}')
result = postfix(expression)
print(f'Postfix : {result}')