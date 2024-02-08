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
from Queue_circular import Queue
from functions import queue_split_alt
# Constants

source = Queue()
temp = Queue()
for i in range(10):
    source.insert(i)
    temp.insert(i)
t1, t2 = queue_split_alt(source)
assert source.is_empty(), "Queue must be empty post split"
print(f"\nt1 contains:")
while not t1.is_empty():
    print(t1.remove(), end=' ')
print(f"\nt2 contains:")
while not t2.is_empty():
    print(t2.remove(), end=' ')
