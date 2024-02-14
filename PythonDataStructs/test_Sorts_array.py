"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
"""
# Imports
import random
from Number import Number
from Sorts_array import Sorts

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
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = []

    for i in range(0,SIZE):
        
        value = Number(i)
            
        values.append(value)   

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    values = []

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
        arrays - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """

    arrays = []
    
    for i in range (0, SIZE):
        array = []
        
        for i in range(0, SIZE):
            x = random.randint(0, XRANGE)
            value = Number(x)
            array.append(value)
            
        arrays.append(array)

    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
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
    arrays = create_randoms()
    count = 0
    for i in arrays:
        func(i)
        count += 1
    
    com3 = Number.comparisons / count
    swap3 = Sorts.swaps / count
    
    
    print('{} {:>9}{:>10}{:>10.0f}{:>10.0f}{:>10.0f}{:>10.0f}'.format(title, com1, com2, com3, swap1, swap2, swap3))
        
    
    return
