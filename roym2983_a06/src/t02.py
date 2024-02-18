"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue
# Constants
pq1, pq2 = Priority_Queue(), Priority_Queue()
for v in [1, 2, 3, 4, 5]:
    pq1.insert(v)
for v in [6, 7, 8, 9, 10]:
    pq2.insert(v)
print(f"pq1 remove : {pq1.remove()}")
print(f"pq1 peek : {pq1.peek()}")
print(f"pq1 empty : {pq1.is_empty()}")
print(f"pq1 len : {len(pq1)}")
t1, t2 = pq2.split_alt()
print("t1 post split_alt : ", ' '.join(str(v) for v in t1))
print("t2 post split_alt : ", ' '.join(str(v) for v in t2))
for v in [5, 4, 3, 2, 1]:
    pq2.insert(v)
k = 5
t3, t4 = pq2.split_key(k)
print(f"t3 post split_key k={k} : ", ' '.join(str(v) for v in t3))
print(f"t4 post split_key k={k} : ", ' '.join(str(v) for v in t4))
cpq = Priority_Queue()
cpq.combine(pq1, t4)
print("cpq post combine pq1 and t4 : ", ' '.join(str(v) for v in cpq))
print("iter cpq : ", ' '.join(str(v) for v in cpq))
