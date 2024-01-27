"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports

# Constants

from Priority_Queue_array import Priority_Queue

source = [5, 4, 3, 2, 1]
pq = Priority_Queue()
for i in source:
    pq.insert(i)
print(f'Source : {source}\n')
print(f'PQ : {pq._values}\n')
while not pq.is_empty():
    pq.remove()
print(f'Post removal source : {source}')
print(f'Post removal PQ : {pq._values}')
