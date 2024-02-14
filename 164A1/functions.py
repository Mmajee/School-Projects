"""
-------------------------------------------------------
functions
-------------------------------------------------------
"""



#1 

def substitute(string, ciphertext):
    """
    -------------------------------------------------------
    Encipher a string using the letter positions in ciphertext.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = substitute(string, ciphertext):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        ciphertext - ciphertext alphabet (str)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    
    plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    estring = ''


    
    for i in string:
        if i not in plaintext:
            estring += i
        for k in range(len(ciphertext)):
            if i == plaintext[k]:
                estring += ciphertext[k]
                
    return estring


#2

def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    
        
    shift = 0
    estring = ''

    plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


   
    for i in range(len(string)):
        if string[i] not in plaintext:
            estring += string[i]

        for k in range(len(plaintext)):
            shift = k + n

            if string[i] == plaintext[k]:
                if shift > (len(plaintext) - 1):
                    shift = len(plaintext) - shift

                estring += plaintext[shift]
            shift = 0

    return estring


#3

def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    
    count1 = 0
    count2 = -1
    s2 = ''
    s = s.lower()
    palindrome = True
    
    for i in s:
        if i.isalpha():
            s2 += i 
    length = len(s2) - 1
  
    
    while palindrome == True and count1 < length:
        
        
        if s2[count1] != s2[count2]:
            palindrome = False
        
        count1 += 1
        count2 -= 1
        
        
        
    return palindrome


#4

def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = False
    
    if year % 4 == 0 and year % 100 != 0: 
        leap_year = True  
    elif year % 400 == 0:
        leap_year = True    
    
    return leap_year


#5

def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a (int)
    -------------------------------------------------------
    """
    
    i = 0
    md = 0
    
    
    while i < (len(a) - 1):
        diff = abs(a[i] - a[i + 1])
        if diff > md:
            md = diff
            
        i += 1
        
    return md
        
        
#6

def transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    
    alist = []
    b = []
    count = 0
    
    
  

    while count < len(a[0]):
        for i in range(len(a)):
            alist.append(a[i][count])

        
        b.append(alist)
        alist = []
        count += 1
        
    return b
    
   
#7

def rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    Use: ra = rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of float)
    Returns:
        ra - the rotated 2D list of values (2D list of float)
    -------------------------------------------------------
    """
    
    alist = []
    ra = []
    count = 0
    
    while count < len(a[0]):
        for i in range(len(a) - 1, -1, -1):
            alist.append(a[i][count])
        
        ra.append(alist)    
        alist = []
        count += 1
    
    return ra

#8

def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains 
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    
    i = 0

    
    while i < (len(values)):
        num = values[0]
        values.remove(num)
        while num in values:
            values.remove(num)
                
        values.append(num)
                          
        i += 1
        
    return
