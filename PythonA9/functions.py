"""
-------------------------------------------------------
functions
-------------------------------------------------------
"""
# 1----------------------------------------------------------------


def file_head(fh, n):
    """
    -------------------------------------------------------
    Prints first n lines of fh. Line numbering starts at 0.
    Use: file_head(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to print (file - open for reading)
        n - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    for _ in range(n):
        lines = fh.readline()
        print(lines.strip())
# 2---------------------------------------------------------------------------


def number_lines(fh_in, fh_out):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_out contain contents
    of fh_in where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: number_lines(fh_in, fh_out)
    -------------------------------------------------------
    Parameters:
        fh_in - file to read (file - open for reading)
        fh_out - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    fh_in.seek(0)

    lines = fh_in.readline()
    count = 0
    while lines != '':
        fh_out.write('[{}] '.format(count) + lines)
        count += 1
        lines = fh_in.readline()

# 3------------------------------------------------------------------------------------------


def get_addresses(fh):
    """
    -------------------------------------------------------
    Reads a addresses from fh into a list of addresses.
    Addresses are stored in fh in the form:
        forename
        surname
        street
        city
        --
    Each address in the list of addresses is a list of the form:
    [forename, surname, street, city]
    Use: addreses = get_addresses(fh)
    -------------------------------------------------------
    Parameters:
        fh - the address file (file - open for reading)
    Returns:
        addresses - the addresses from fh (str)
    -------------------------------------------------------
    """
    fh.seek(0)

    lines = fh.readline()
    addresses = []
    alist = []
    count = 0

    while lines != '':

        if lines.strip() != '--' and count < 4:

            alist.append(lines.strip())

        if count == 3:
            addresses.append(alist)
            alist = []
            count = -2

        count += 1
        lines = fh.readline()

    return addresses

# 4----------------------------------------------------------------------------------------------


def merge_letters(fh_letter, fh_addresses, fh_merged):
    """
    -------------------------------------------------------
    Merges a letter with a list of addresses.
    Writes the results to a file of completed letters.
    Use: merge_letters(fh_letter, fh_addresses, fh_merged)
    -------------------------------------------------------
    Parameters:
        fh_letter - a file with a letter to process (file - open for reading)
        fh_addresses - a file of addresses (file - open for reading)
        fh_merged - a file of merged letters (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    fh_letter.seek(0)

    alist = []
    astring = ''
    astring2 = ''
    count = 0
    count2 = 0
    addresses = get_addresses(fh_addresses)
    address = addresses[0]

    lines2 = fh_letter.readline()

    while lines2 != '':

        lines2 = lines2.split()

        for i in lines2:

            print(i)

            # if i[0] == '[' and i[-1] != ']':

            if i == '[forename]':
                fh_merged.write(address[0] + ' ')
                astring = ''

            elif i == '[surname]':
                fh_merged.write(address[1] + ' ')
                astring = ''

            elif i == '[street]':
                fh_merged.write(address[2] + ' ')
                astring = ''

            elif i == '[city]':
                fh_merged.write(address[3] + ' ')
                astring = ''
            else:
                fh_merged.write(i + ' ')
                astring = ''

        fh_merged.write('\n')
        lines2 = fh_letter.readline()


# 5--------------------------------------------------------------------------------------------


def student_info(students):
    """
    -------------------------------------------------------
    Get information from a file of students and grades.
    Use: l_id, h_id, avg = student_info(students)
    -------------------------------------------------------
    Parameters:
        students - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """

    lines = students.readline()
    alist = lines.strip().split(',')
    l_id = alist[2]
    h_id = alist[2]
    minimum = int(alist[3])
    maximum = int(alist[3])

    total = 0
    count = 0

    while lines != '':

        total += int(alist[3])
        count += 1

        if int(alist[3]) < minimum:
            minimum = int(alist[3])
            l_id = alist[2]

        if int(alist[3]) > maximum:
            maximum = int(alist[3])
            h_id = alist[2]

        lines = students.readline()
        alist = lines.strip().split(',')

    avg = total / count

    return l_id, h_id, avg

# 6---------------------------------------------------------------------------------


def substitute(fh_in, fh_out, ciphertext):
    """
    -------------------------------------------------------
    Encipher a file using the letter positions in ciphertext.
    Only letters are enciphered, and the resulting strings are
    in upper case.
    Use: substitute(fh_in, fh_out, ciphertext)
    -------------------------------------------------------
    Parameters:
        fh_in - input file (file - open for reading)
        fh_out - output file (file - open for writing)
        ciphertext - ciphertext alphabet (str)
    Returns:
        None
    -------------------------------------------------------
    """
    fh_in.seek(0)
    plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    lines = fh_in.readline()

    lines = lines.upper()

    while lines != '':
        for i in lines:
            if i not in plaintext:
                fh_out.write(i)
            for k in range(len(ciphertext)):
                if i == plaintext[k]:
                    fh_out.write(ciphertext[k])

        lines = fh_in.readline()

        lines = lines.upper()


# 7-------------------------------------------------------------------------------

def shift(fh_in, fh_out, n):
    """
    -------------------------------------------------------
    Encipher a file using a shift cipher.
    Only letters are enciphered, and the resulting strings are
    in upper case.
    Use: shift(fh_in, fh_out, n)
    -------------------------------------------------------
    Parameters:
        fh_in - input file (file - open for reading)
        fh_out - output file (file - open for writing)
        n - the number of letters to shift (int)
    Returns:
        None
    -------------------------------------------------------
    """
    fh_in.seek(0)
    shift = 0

    plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    lines = fh_in.readline()
    lines = lines.upper()

    while lines != '':
        for i in range(len(lines)):
            if lines[i] not in plaintext:
                fh_out.write(lines[i])

            for k in range(len(plaintext)):
                shift = k + n

                if lines[i] == plaintext[k]:
                    if shift > (len(plaintext) - 1):
                        shift = len(plaintext) - shift

                    fh_out.write(plaintext[shift])
                shift = 0

        lines = fh_in.readline()

        lines = lines.upper()
