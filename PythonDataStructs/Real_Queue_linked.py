"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------
"""
from copy import deepcopy


class _Queue_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """

        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """

        return self._count != 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """

        new_node = _Queue_Node(value, None)
        
        if self._rear is None:
            self._rear = new_node
            self._front = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node
        
        self._count += 1
        

        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------        
        """
        assert self._front is not None, "Cannot remove from an empty queue"


        value = self._front._value
        
        self._front = self._front._next
        
        if self._rear is None:
            self._rear = self._front

        self._count -= 1
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"


        value = deepcopy(self._front._value)

        return value

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated. Equivalent of:
        self.insert(source.remove()), but moves nodes not data.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty queue"


        node = source._front
        
        source._front = source._front._next
        source._count -= 1
        
        
        if source._front is None:
            source._rear = None
                
        
        if self._rear is None:
            self._front = node
            self._rear = node
            self._rear._next = None
        else:
            self._rear._next = node
            self._rear = node
            self._rear._next = None

        self._count += 1
        
        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"

        
        while source._count > 0:
            self._move_front_to_rear(source)


        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """

        while source1._count > 0 or source2._count > 0:
            if source1._count > 0:
                self._move_front_to_rear(source1)
            
            if source2._count > 0:
                self._move_front_to_rear(source2)

        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains remaining values from source (Queue)
        -------------------------------------------------------
        """
        target1 = Queue()
        target2 = Queue()
        left = True
        
        while self._front is not None:    
            
            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
                  
            left = not left

        
        return target1, target2

    def is_identical(self, target):
        """
        -------------------------------------------------------
        Determines whether two queues are identical.
        Values of self and target are compared and if all contents 
        are identical and in the same order, returns True, otherwise 
        returns False. Queues are unchanged.
        (iterative algorithm)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False 
                otherwise. (boolean)
        -------------------------------------------------------
        """

        identical = True
        
        if self._count != target._count:
            identical = False
        else:      
            current = self._front
            current2 = target._front
            
            while current is not None and current._value == current2._value:
                current = current._next
                current2 = current2._next
                
            if current is not None:
                identical = False

        return identical

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
