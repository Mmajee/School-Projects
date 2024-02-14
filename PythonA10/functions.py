"""
-------------------------------------------------------
functions 
-------------------------------------------------------
"""
# 1-------------------------------------------------------------------------------------------


def binary_search(values, key):
    """
    -------------------------------------------------------
    Searches for the first occurrence of key in the sorted list
    values. Returns -1 if key is not found.
    Use: i = binary_search(values, key)
    -------------------------------------------------------
    Parameters:
        values - a list of data (sorted list of ?)
        key - a data element (?)
    Returns:
        i - the index of the first occurrence of key in
            the list, -1 if key is not found. (int)
    -------------------------------------------------------
    """

    found = False
    newlist = values
    count = 1
    count2 = 0

    while found == False:

        middle = len(newlist) // 2
        print(middle)

        if len(newlist) == count:
            if newlist[count2] == key:
                i = count
                found = True
            else:
                i = -1
                found = True

        if key > values[middle]:
            newlist = values[middle:]

        else:
            newlist = values[0:middle]
            print(newlist)

    return i

# 2----------------------------------------------------------------------------------------------------


def flatten(values):
    """
    -------------------------------------------------------
    Flattens a 2D list. Creates a new 1D list from values.
    Use: flattened = flatten(values)
    -------------------------------------------------------
    Parameters:
        values - a 2D list of data (list of list of ?)
    Returns:
        flattened - a 1D list of flattened values (list ?)
    -------------------------------------------------------
    """

    flattened = []

    for i in values:
        for k in i:
            flattened.append(k)

    return flattened


# 3------------------------------------------------------------------------------------------------

def matrix_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies a by b. Matrices are multiplied by taking the dot product
    of the rows of a against the columns of b.
    Rows of a == columns of b, columns of a == rows of b.
    See: https://en.wikipedia.org/wiki/Matrix_multiplication
    Use: c = matrix_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - the matrix to multiply (2D list of int/float)
        b - the matrix to multiply by (2D list of int/float)
    Returns:
        c - the resulting matrix of a times b
            (2D list of int/float)
    ------------------------------------------------------
    """

    length1 = len(a[0])
    length2 = len(b)
    c = []
    dot = 0

    if length1 == length2:
        for i in range(length1):
            print(i, '-')
            for k in range(length2):
                print(k)
                x = a[0][k] * b[k][0]
                dot += x
                print(dot)
            c.append(dot)
            dot = 0
            print(c)
