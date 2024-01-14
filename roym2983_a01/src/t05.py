"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
# Imports
from functions import is_leap_year
# Constants

year_to_check = 2024
if is_leap_year(year_to_check):
    print(f"{year_to_check} is a leap year")
else:
    print(f"{year_to_check} isn't a leap year")
