"""
-------------------------------------------------------
Assignment 5, Task 2
-------------------------------------------------------
"""
from Sorted_List_array import Sorted_List
from utilities import array_to_list

source = [11,22,33,44,55,66]
llist = Sorted_List()

for i in source:
    llist.insert(i)
    
for i in llist:
    print(i)
    
key = 44

target1, target2 = llist.split_key(key)
print()
print(target1)
print(target2)

    
