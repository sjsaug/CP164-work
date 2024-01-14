"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Your Name
ID:      Your ID
Email:   your email@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze
# Constants

fh = open("t04.txt", "r", encoding="utf-8")
upper, lower, digit, white, remain = file_analyze(fh)
print(f"""
Uppercase:  {upper}
Lowercase:  {lower}
Digits:     {digit}
Whitespaces: {white}
Remaining:  {remain}""")
