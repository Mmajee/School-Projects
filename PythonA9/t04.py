"""
-------------------------------------------------------
Assignment 9, Task 4
-------------------------------------------------------
"""
from functions import merge_letters

fh_letter = open('letter.txt', 'r')

fh_addresses = open('addresses.txt', 'r')

fh_merged = open('merged.txt', 'a')

merge_letters(fh_letter, fh_addresses, fh_merged)

fh_letter.close()
fh_addresses.close()
fh_merged.close()
