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
# Constants

q1 = Queue()
q2 = Queue()
for element in range(1, 10):
    q1.insert(element)
    q2.insert(element)
if q1.__eq__(q2):
    print("Queues equal")
else:
    print("Queues not equal")