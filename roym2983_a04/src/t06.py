"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
# Constants


pq = Priority_Queue()
for value in [5, 10, 15, 25, 15, 20]:
    pq.insert(value)
key = 15
h, lw = pq.split_key(key)
pq_elements = [str(value) for value in pq]
print(f"pq contains: {' '.join(pq_elements)}")
h_elements = [str(value) for value in h]
print(f"h contains: {' '.join(h_elements)}")