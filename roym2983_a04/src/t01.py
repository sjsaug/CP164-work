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

q = Queue()

for i in range(10):
    q.insert(i)
    print(f"Inserted {i}")
if q.is_empty():
    print("Queue empty")
if q.is_full():
    print("Queue full")
f1 = q.peek()
print(f"{f1} is the first element")
removed = q.remove()
print(f"Removed {removed} from queue")
q2 = Queue()
for i in range(5):
    q2.insert(i)
if q == q2:
    print("queue equal to queue2")
