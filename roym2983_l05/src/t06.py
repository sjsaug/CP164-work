"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-02-10"
-------------------------------------------------------
"""
# Imports
from functions import bag_to_set
# Constants

print(f"bag_to_set([4, 5, 3, 4, 5, 2, 2, 4]) = {bag_to_set([4, 5, 3, 4, 5, 2, 2, 4])} | expected = [4, 5, 3, 2]")
print(f"bag_to_set([1, 1, 1, 1, 1]) = {bag_to_set([1, 1, 1, 1, 1])} | expected = [1]")
print(f"bag_to_set([]) = {bag_to_set([])} | expected = []")