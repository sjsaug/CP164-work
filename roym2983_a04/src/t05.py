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
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue
# Constants


pq = Priority_Queue()
pq.insert(5)
pq.insert(4)
pq.insert(3)
pq.insert(1)
split_key = 4
h, lw = pq_split_key(pq, split_key)
h_elements = [str(value) for value in h]
print(f"h contains: {' '.join(h_elements)}")
lw_elements = [str(value) for value in lw]
print(f"lw contains: {' '.join(lw_elements)}")