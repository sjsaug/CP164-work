"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import stack_test
from Food_utilities import read_food
# Constants

stack = Stack()
fh = open("foods.txt", "r", encoding="utf-8")
for line in fh:
    food = read_food(line)
    stack.push(food)

stack_test(stack)