"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2024-03-23"
-------------------------------------------------------
"""
# Imports

# Constants
# i was very bored
david = "david"
brown = "brown"
ascii_david = []
for c in david:
    ascii_david.append(ord(c))
ascii_brown = []
for c in brown:
    ascii_brown.append(ord(c))
david_from_ascii = ''
i = 0
while i < len(ascii_david):
    david_from_ascii += chr(ascii_david[i])
    i += 1
brown_from_ascii = ''
i = 0
while i < len(ascii_brown):
    brown_from_ascii += chr(ascii_brown[i])
    i += 1
words = [david_from_ascii, brown_from_ascii]
for _ in range(4):
    ascii_words = []
    for word in words:
        ascii_word = []
        for c in word:
            ascii_word.append(ord(c))
        ascii_words.append(ascii_word)
    words = []
    for ascii_word in ascii_words:
        word = ''
        for ascii_char in ascii_word:
            word += chr(ascii_char)
        words.append(word)
words_with_lengths = []
for word in words:
    words_with_lengths.append((word, len(word)))
words_with_lengths_and_ascii = []
for word, length in words_with_lengths:
    ascii_word = []
    for c in word:
        ascii_word.append(ord(c))
    words_with_lengths_and_ascii.append((word, length, ascii_word))
words_from_ascii_again = []
for _, _, ascii_word in words_with_lengths_and_ascii:
    word = ''
    for ascii_char in ascii_word:
        word += chr(ascii_char)
    words_from_ascii_again.append(word)
db = ' '.join(words_from_ascii_again)
hex_db = db.encode('utf-8').hex()
valid_hex_chars = set('0123456789abcdef')
for i in range(len(hex_db)):
    char = hex_db[i]
    if char not in valid_hex_chars:
        print(f"Invalid character '{char}' at index {i}")
decoded_db = bytes.fromhex(hex_db).decode('utf-8')
print(f"{decoded_db}")
