"""
-------------------------------------------------------
Tests various linked sorting functions.
-------------------------------------------------------
"""
# Imports
import random

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    values = List()

    for i in range(0,SIZE):
        
        value = Number(i)
            
        values.append(value)   

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    values = List()

    for i in range(SIZE - 1, -1, -1):
        
        value = Number(i)
            
        values.append(value)       

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """

    Lists = List()
    
    for i in range (0, SIZE):
        sList = List()
        
        for i in range(0, SIZE):
            x = random.randint(0, XRANGE)
            value = Number(x)
            sList.append(value)
            
        Lists.append(sList)

    return Lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    Sorts.swaps = 0   
    Number.comparisons = 0
    values = create_sorted()
    func(values)
    com1 = Number.comparisons
    swap1 = Sorts.swaps
    
    
    Sorts.swaps = 0   
    Number.comparisons = 0
    values = create_reversed()
    func(values)
    com2 = Number.comparisons
    swap2 = Sorts.swaps
    
    Sorts.swaps = 0
    Number.comparisons = 0
    Lists = create_randoms()
    count = 0
    for i in Lists:
        func(i)
        count += 1
        
    com3 = Number.comparisons / 2    
    swap3 = Sorts.swaps
    
    
    print('{} {:>10}{:>10}{:>10.0f}{:>10.0f}{:>10.0f}{:>10.0f}'.format(title, com1, com2, com3, swap1, swap2, swap3))
        

    return
