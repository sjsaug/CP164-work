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
from Queue_array import *
# Constants

q = Queue()
for i in range(10):
    q.insert(i)
t1, t2 = q.split_alt()
t1_elements = [str(value) for value in t1]
print(f"t1 contains: {' '.join(t1_elements)}")
t2_elements = [str(value) for value in t2]
print(f"t2 contains: {' '.join(t2_elements)}")
