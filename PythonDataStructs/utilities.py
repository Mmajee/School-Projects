
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List

s = Stack()
stack = Stack()

def array_to_stack(s, a):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack, 
    first value in source is on top of stack.
    Use: array_to_stack(s, a)
    -------------------------------------------------------
    Parameters:
        s - a Stack object (Stack)
        a - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    b = s.is_empty()
    length = len(a)
    
    if b == False:
        s = Stack()

    while i < length:
        x = a.pop(-1)
        s.push(x)
        i += 1    
    return
    
def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    b = stack.is_empty()

    while b == False:
        x = stack.pop()
        target.insert(0,x)
        b = stack.is_empty()
        
    return 


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and 
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    b = source.is_empty()
    
    source.pop()
    
    source.push()
    
    source.peek()
    
    return



def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue, 
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    i = 0
    length = len(source) 
    
    while i < length:
        x = source.pop(0)
        queue.insert(x)
        i += 1
        
    return

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    i = 0
    
    length = len(queue)
    
    while i < length:
        x = queue.remove()
        target.append(x)
        i += 1

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq, 
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    i = 0
    
    length = len(source)
    
    while i < length:
        x = source.pop(0)
        pq.insert(x)
        i += 1
        
    return

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    i = 0
    
    length = len(pq)
    
    while i < length:
        x = pq.remove()
        target.append(x)
        i += 1

    return

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        the methods of Queue are tested for both empty and 
        non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    -------------------------------------------------------
    """
    q = Queue()
    
    for i in a:
        q.insert(i)
    
    print(q)
    
    p = q.remove()
    print(p)
    
    b = q.is_empty()
    print(b)
    
    c = q.peek()
    print(c)
 
    k = len(q)
    print(k)
    
    return 


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Use: pq_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        the methods of Priority_Queue are tested for both empty and 
        non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    for i in a:
        pq.insert(i)  
    print(pq)
    
    p = pq.remove()
    print(p)
    
    b = pq.is_empty()
    print(b)
    
    c = pq.peek()
    print(c)
 
    k = len(pq)
    print(k)

    return

def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist, 
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    
    length = len(source)
    
    while i < length:
        x = source.pop(0)
        llist.append(x)
        i += 1
        
    return
    
    

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    
    length = len(llist)
    
    while i < length:
        x = llist.pop(0)
        target.append(x)
        i += 1
        
    return

def list_test(a):
    """
    -------------------------------------------------------
    Tests list implementation.
    The methods of List are tested for both empty and 
    non-empty lists using the data in a:
    is_empty, insert, remove, append, index, __contains__,
    find, count, max, min, __getitem__, __setitem__
    Use: list_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    b = lst.is_empty()
    
    for i in range(a):
        lst.insert(i, a[i])
        
    key = 0
        
    lst.remove(key)
    
    for i in range(a):
        lst.iappend(a[i])
        
    c = lst.index(key)
    
    k = key in lst
    
    k = lst.find(key)
    
    k = lst.count(key)
    
    k = lst.max()
    k = lst.min()
    
    p = 0
    
    k = lst[p]
    
    lst[p] = key

    lst.append(key)
    return
