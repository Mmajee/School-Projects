"""
-------------------------------------------------------
functions
-------------------------------------------------------
"""
# 1----------------------------------------------------------------------------------


def my_isdigit(s):
    """
    -------------------------------------------------------
    Determines if all the characters is s are digits. An empty string
    has no digits.
    NOTE: must execute as the equivalent of the Python method s.isdigit()
    Use: digits = my_isdigit(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        digits - True if all of s is digits, False otherwise (boolean)
    -------------------------------------------------------
    """
    digits = True
    count = 0
    numbers = '0123456789'

    while digits and count < len(s):

        if s[count] not in numbers:
            digits = False
        count += 1

    return digits


# 2------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def my_isalpha(s):
    """
    -------------------------------------------------------
    Determines if all the characters is s are alphabetic characters.
    An empty string has no letters.
    NOTE: must execute as the equivalent of the Python method s.isalpha()
    Use: alpha = my_isalpha(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        alpha - True if all of s is letters of the alphabet,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    alpha = True

    count = 0
    letters = 'abcdefghigklmnopqrstuvwxyz'

    while alpha and count < len(s):
        if s[count] not in letters and s[count] not in letters.upper():
            alpha = False
        count += 1

    return alpha

# 3-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def my_find(s, r):
    """
    -------------------------------------------------------
    Returns the index of the string r in the string s.
    NOTE: must execute as the equivalent of the Python method s.find(r)
    Use: i = my_find(s, r)
    -------------------------------------------------------
    Parameters:
        s - a string to search (str)
        r - a string to search for (str)
    Returns:
        i - the index of the start of r in s, -1 if r is not in s (int)
    -------------------------------------------------------
    """
    count = 0
    i = -1

    while count < len(s) and i == -1:

        if r in s and r[0] == s[count]:
            i = count

        count += 1

    return i

# 4-------------------------------------------------------------------------------------


def common_ending(s1, s2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string for ending comparison (str)
        s2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of s1 and s2 (str)
    -------------------------------------------------------
    """
    count1 = len(s1) - 1
    count2 = len(s2) - 1

    while s1[count1] == s2[count2] and count1 >= 0 and count2 >= 0:
        count1 -= 1
        count2 -= 1

    common = s1[count1 + 1:len(s1)]

    return common

# 5------------------------------------------------------------------------------------------


def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """

    valid = True

    count = 0
    dashes = 0

    while valid and count < len(isbn):

        if isbn[count] == '-':
            dashes += 1

        if isbn[count].isalpha():
            valid = False

        elif isbn[0:3] != '978' and '979':
            valid = False

        elif isbn[-2] != '-':
            valid = False

        elif len(isbn) != 17:
            valid = False

        elif isbn[count:count + 2] == '--':
            valid = False

        count += 1

    if dashes != 4:
        valid = False

    return valid

# 6----------------------------------------------------------------------------------------------------


def number_convert(number):
    """
    -------------------------------------------------------
    Converts a phone number character string to a string of digits.
    A telephone keypad has the following digit/letter combinations:
        2 : ABC
        3 : DEF
        4 : GHI
        5 : JKL
        6 : MNO
        7 : PRS
        8 : TUV
        9 : WXY
    ('Q' and 'Z' are not represented.) Q, Z, and non-letters are
    left unchanged.
    Use: digits = number_convert(number)
    -------------------------------------------------------
    Parameters:
        number - a phone number string (str)
    Returns:
        digits - the numeric version of number based upon a
            telephone keypad (str)
    -------------------------------------------------------
    """

    digits = ''
    count = 0

    while not number.isdigit() and count < len(number):

        if number[count] == 'A' or number[count] == 'B' or number[count] == 'C':

            digits += '2'

        elif number[count] == 'D' or number[count] == 'E' or number[count] == 'F':

            digits += '3'

        elif number[count] == 'G' or number[count] == 'H' or number[count] == 'I':

            digits += '4'

        elif number[count] == 'J' or number[count] == 'K' or number[count] == 'L':

            digits += '5'

        elif number[count] == 'M' or number[count] == 'N' or number[count] == 'O':

            digits += '6'

        elif number[count] == 'P' or number[count] == 'R' or number[count] == 'S':

            digits += '7'

        elif number[count] == 'T' or number[count] == 'U' or number[count] == 'V':

            digits += '8'

        elif number[count] == 'W' or number[count] == 'X' or number[count] == 'Y':

            digits += '9'

        else:
            digits += number[count]
        count += 1

    return digits

# 7-------------------------------------------------------------------------------------------------


def pluralize(s):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if s ends with 's', 'sh', or 'ch', add 'es'
        - if s ends with 'y' but not 'ay' or 'oy', add 'ies'
        - otherwise add 's'
    Use: plural = pluralize(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        plural - a plural version of s (str)
    -------------------------------------------------------
    """

    plural = ''

    length = len(s)

    for i in range(len(s) - 1):
        plural += s[i]

    if s[-1] == 's' or s[-2:] == 'sh' or s[-2:] == 'ch':
        plural += s[length - 1] + 'es'

    elif s[-1] == 'y' and s[-2:] != 'ay' and s[-2:] != 'oy':
        plural += 'ies'
    else:
        plural += s[length - 1] + 's'

    return plural
