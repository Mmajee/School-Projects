"""
-------------------------------------------------------
functions
-------------------------------------------------------
"""
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue

def queue_is_identical(source1, source2):
    """
    ----------------
    Determines whether two given queues are identical. Entries of 
    source1 and source2 are compared and if all contents are identical
    and in the same order, returns True, otherwise returns False.
    Use: identical = queue_is_identical(source1, source2)
    ---------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        identical - True if source1 and source2 are identical, False otherwise. 
            source1 and source2 are unchanged. (boolean)
    ---------------
    """
    
    i = 0
    identical = True
    
    
    if len(source1) != len(source2):
        identical = False
    else:
        length = len(source1)
    
    while identical == True and i < length:
        x = source1.remove()
        y = source2.remove()
        
        if x != y:
            identical = False 
        i += 1 

    return identical
        
        
def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends. The order of the values from source is preserved.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    
    i = 0
    length = len(source)
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    while i < length:
        
        x = source.remove()
        
        if x > key:
            target1.insert(x)
        else:
            target2.insert(x)
        
        i += 1
        
        
    return target1, target2
