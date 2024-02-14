"""
-------------------------------------------------------
Assignment 4, Task 2
-------------------------------------------------------
"""
from utilities import array_to_queue
from Queue_array import Queue

a = [0,1,2,3,4,5]
a2 = [0,1,2,3,4,6]
print(a)
print(a2)

source1 = Queue()
array_to_queue(source1, a) 
source2 = Queue()
array_to_queue(source2, a2)
identical = source1.is_identical(source2)

print()
if identical == True:
    print('source1 and source2 are identical')
else:
    print('source1 and source2 are not identical')
