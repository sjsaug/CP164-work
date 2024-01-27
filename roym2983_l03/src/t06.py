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
from utilities import array_to_pq
from utilities import pq_to_array
from utilities import priority_queue_test

source = [1, 2, 3, 4, 5]
pq = Priority_Queue()
print(f'Source : {source}\n')
print(f'Queue : {pq._values}\n')
array_to_pq(pq, source)
print(f'Source : {source}\n')
print(f'Queue : {pq._values}\n')
print(f'Source : {source}\n')
print(f'Queue : {pq._values}\n')
pq_to_array(pq, source)
print(f'Source : {source}\n')
print(f'Queue : {pq._values}\n')
priority_queue_test(source)
