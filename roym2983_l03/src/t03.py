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
from Queue_array import Queue
from utilities import array_to_queue
from utilities import queue_to_array
from utilities import queue_test

source = [1, 2, 3, 4, 5]
queue = Queue()

print(f'Source : {source}')
print(f'Queue : {queue._values}\n')
array_to_queue(queue, source)
print(f'Source : {source}\n')
print(f'Queue : {queue._values}\n')
print(f'Source : {source}\n')
print(f'Queue : {queue._values}\n')
queue_to_array(queue, source)
print(f'Source : {source}\n')
print(f'Queue : {queue._values}\n')
queue_test(source)