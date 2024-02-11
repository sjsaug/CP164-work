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
from Sorted_List_array import Sorted_List
from Food import Food
from Food_utilities import *
# Constants

# setup sorted lists
list1 = Sorted_List()
list2 = Sorted_List()

# setup food sorted list
fh = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fh)
fL = Sorted_List()
for food in foods:
    fL.append(food)

# Test __contains__
list1.append(1)
print(f'1 in list1: {1 in list1}')  # Expected output: True

# Test __eq__
list1.append(1)
list2.append(1)
print(f'list1 == list2: {list1 == list2}')  # Expected output: True

# Test __getitem__
list1.append(2)
print(f'list1[1]: {list1[1]}')  # Expected output: 2

# Test clean
list1.append(2)
list1.clean()
print(f'list1 after clean: {list1}')  # Expected output: [1, 2]

# Test count
list1.append(1)
print(f'count of 1 in list1: {list1.count(1)}')  # Expected output: 2

# Test find
print(f'find 1 in list1: {list1.find(1)}')  # Expected output: 1

# Test index
print(f'index of 1 in list1: {list1.index(1)}')  # Expected output: 0

# Test intersection
list2.append(1)
# Expected output: [1]
print(f'intersection of list1 and list2: {list1.intersection(list2)}')

# Test max
print(f'max of list1: {list1.max()}')  # Expected output: 2

# Test min
print(f'min of list1: {list1.min()}')  # Expected output: 1

# Test peek
print(f'peek of fL: {fL.peek()}')  # Expected output: N/A

# Test remove
list1.remove(1)
print(f'list1 after remove: {list1}')  # Expected output: [2]

# Test remove_front
list1.remove_front()
print(f'list1 after remove_front: {list1}')  # Expected output: []

# Test remove_many
list1.append(1)
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

# Test split_key
list1.append(3)
list2, list3 = list1.split_key(2)
print(f'list2 after split_key: {list2}')  # Expected output: [1, 2]
print(f'list3 after split_key: {list3}')  # Expected output: [3]

# Test union
list2.append(3)
list1.union(list2)
print(f'list1 after union: {list1}')  # Expected output: [1, 2, 3]
