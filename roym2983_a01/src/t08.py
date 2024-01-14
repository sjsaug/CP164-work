"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Your Name
ID:      Your ID
Email:   your email@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats
# Constants

matrix = [
    [1.2, 3.2, 4.3],
    [7.9, 2.6, 2.1],
    [6.1, 9.3, 7.6]]

smallest, largest, total, avg = matrix_stats(matrix)
print(f"Smallest : {smallest}")
print(f"Largest : {largest}")
print(f"Total : {total}")
print(f"Average : {avg}")
