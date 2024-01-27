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

source = [1, 2, 3, 4, 5]
queue = Queue()

for i in source:
    queue.insert(i)

print(f'Contents in queue : {queue._values} \n')

value = queue.peek()

print(f'Top of queue : {value}')

while not queue.is_empty():
    queue.remove()

print(f'Post removal : {queue._values}')
