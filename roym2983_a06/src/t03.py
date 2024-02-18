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
from Deque_linked import Deque
# Constants
d = Deque()
for v in [1, 2, 3, 4, 5]:
    d.insert_rear(v)
print("d post insert rear : ", ' '.join(str(v) for v in d))
for v in [0, -1, -2, -3, -4]:
    d.insert_front(v)
print("d post insert front : ", ' '.join(str(v) for v in d))
fv, rv = d.remove_front(), d.remove_rear()
print(f"d remove front : {fv}, d remove rear : {rv}")
fp, rp = d.peek_front(), d.peek_rear()
print(f"d peek front : {fp}, d peek rear : {rp}")
print(f"d empty : {d.is_empty()}")
print(f"d len : {len(d)}")
d2 = Deque()
for v in [-2, -1, 0, 1, 2, 3, 4]:
    d2.insert_rear(v)
print(f"d equal d2 : {d == d2}")
print("iter d : ", ' '.join(str(v) for v in d))
