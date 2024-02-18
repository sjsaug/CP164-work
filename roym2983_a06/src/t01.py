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
from Queue_linked import Queue
# Constants

q1, q2, q3 = Queue(), Queue(), Queue()
for i in range(1, 5):
    q1.insert(i)
for i in range(5, 10):
    q2.insert(i)
print(f"Q1 empty : {q1.is_empty()}")
print(f"Q2 empty : {q2.is_empty()}")
print(f"Q1 peek : {q1.peek()}")
print(f"Q2 peek : {q2.peek()}")
print(f"Q1 remobe : {q1.remove()}")
print(f"Q2 remove : {q2.remove()}")
q3.combine(q1, q2)
print("Q3 combine : Q1 and Q2 : ", ' '.join(str(v) for v in q3))
q1, q2 = q3.split_alt()
print("Q1 splitting Q3 : ", ' '.join(str(v) for v in q1))
print("Q2 splitting Q3 : ", ' '.join(str(v) for v in q2))
print(f"Q1 len : {len(q1)}")
print(f"Q2 len : {len(q2)}")
q1._append_queue(q2)
print("Q1 post append of Q2 : ", ' '.join(str(v) for v in q1))
new_q = Queue()
new_q.insert(1)
print(f"Q1 equal nq : {q1 == new_q}")
new_q._append_queue(q1)
print(f"Q1 equal to nq post append : {q1 == new_q}")