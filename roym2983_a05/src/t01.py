"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-02-11"
-------------------------------------------------------
"""
# Imports
from List_array import List
from Food_utilities import *
from Food import Food
# Constants

# setup food list
fh = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fh)
fL = List()
for food in foods:
    fL.append(food)

# setup normal lists
list1 = List()
list2 = List()

# Test __eq__
list1.append(1)
list2.append(1)
print(f'list1 == list2: {list1 == list2}')  # Expected output: True

# Test __getitem__
list1.append(2)
print(f'list1[1]: {list1[1]}')  # Expected output: N/A

# Test append
list1.append(3)
print(f'list1[2]: {list1[2]}')  # Expected output: 3

# Test clean
list1.append(3)
list1.clean()
print(f'list1 after clean: {list1}')  # Expected output: [1, 2, 3]

# Test combine
list2.append(4)
list1.combine(list2)
print(f'list1 after combine: {list1}')  # Expected output: [1, 2, 3, 4]

# Test intersection
list1 = List()
list2 = List()
list1.append(1)
list2.append(1)
list1.intersection(list1, list2)
print(f'list1 after intersection: {list1}')  # Expected output: [1]

# Test prepend
list1.prepend(0)
print(f'list1[0] after prepend: {list1[0]}')  # Expected output: 0

# Test remove_front
fL.remove_front()
print(f'fL[0] after remove_front: {fL[0]}')  # Expected output: 1

# Test remove_many
list1.append(1)
list1.remove_many(1)
print(f'list1 after remove_many: {list1}')  # Expected output: []

# Test split
list1.append(1)
list1.append(2)
list2, list3 = list1.split()
print(f'list2 after split: {list2}')  # Expected output: [1]
print(f'list3 after split: {list3}')  # Expected output: [2]

# Test split_alt
list1.append(1)
list1.append(2)
list2, list3 = list1.split_alt()
print(f'list2 after split_alt: {list2}')  # Expected output: [1]
print(f'list3 after split_alt: {list3}')  # Expected output: [2]

# Test union
list1.append(1)
list2.append(2)
list1.union(list2)
print(f'list1 after union: {list1}')  # Expected output: [1, 2]
