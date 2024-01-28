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
from functions import stack_maze
# Constants
maze = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': [
    'D', 'E'], 'D': [], 'E': ['F', 'X'], 'F': ['G', 'H'], 'G': [], 'H': []}
print(f"Maze : {maze}\n")
maze2 = stack_maze(maze)
print(f"Stack Maze : {maze2}\n")