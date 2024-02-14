"""
-------------------------------------------------------
functions
-------------------------------------------------------
"""

from random import randint

CATEGORIES = (100, 200, 300, 400)

ONES = ('one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine')
TEENS = ('eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
         'sixteen', 'seventeen', 'eighteen', 'nineteen')
TENS = ('ten', 'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety')


# 1------------------------------------------------------------------------------------------------


def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set. Element order is preserved.
    A bag is a list that may contain many copies of a value.
    A set is a list that may contain only one copy of a value.
    bag is left unchanged.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list that main contain duplicates (list of ?)
    Returns:
        new_set - contains one each of the elements in bag (list of ?)
    -------------------------------------------------------
    """
    new_set = []
    count = 0

    while count < len(bag):
        if bag[count] not in new_set:
            new_set.append(bag[count])
        count += 1

    return new_set


# 2--------------------------------------------------------------------------------------------------

def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list. At finish, values
    contains only one copy of each of its original elements.
    Order is preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    count = 0
    alist = []

    LENGTH = len(values)

    while count < LENGTH:

        x = values.pop()
        alist.append(x)

        count += 1

    for i in range(LENGTH - 1, 0, -1):
        if alist[i] not in values:
            values.append(alist[i])

    print('Cleaned: {}'.format(values))


# 3--------------------------------------------------------------------------------------------

def two_element_subset(string):
    """
    -------------------------------------------------------
    Creates a list of all two-element subsets of the characters
    of a string.
    Use: subsets = two_element_subset(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        subsets - a list of two element subsets of s (list of str)
    -------------------------------------------------------
    """

    subsets = []
    string2 = string[0]
    count = 1
    count2 = 1
    count3 = 0

    while count < (len(string)):
        string2 += string[count]
        subsets.append(string2)

        if count == (len(string) - 1):
            count = count2
            count2 += 1
            count3 += 1

        string2 = string[count3]

        count += 1

    return subsets

# 4----------------------------------------------------------------------------------------------


def set_trials(subjects):
    """
    -------------------------------------------------------
    Assignments members of subjects randomly to either a trial of a drug
    or a trial of a placebo. Half the subjects should end up in the drug
    trial and the other half in the placebo trial. For an odd number of
    subjects the 'extra' member can be assigned to either the drug trial
    or the placebo trial. subjects is empty when finished.
    Use: drugs, placebos = set_trials(subjects)
    -------------------------------------------------------
    Parameters:
        subjects - a list of subjects for a drug trial (list of ?)
    Returns:
        drugs - list of subjects assigned to the drug trial (list of ?)
        placebos - list of subjects assigned to the placebo trial (list of ?)
    -------------------------------------------------------
    """

    count = 0
    drugs = []
    placebos = []
    half = len(subjects) // 2

    while count < len(subjects):
        randNum = randint(0, len(subjects) - 1)
        randlist = randint(0, 1)

        if len(subjects) % 2 != 0 and count == len(subjects) - 1:
            if randlist == 0:
                drugs.append(subjects[randNum])
                count += 1
            elif randlist == 1:
                placebos.append(subjects[randNum])
                count += 1

        elif randlist == 0 and subjects[randNum] not in drugs and subjects[randNum] not in placebos and len(drugs) != half:
            drugs.append(subjects[randNum])
            count += 1
        elif randlist == 1 and subjects[randNum] not in placebos and subjects[randNum] not in drugs and len(placebos) != half:
            placebos.append(subjects[randNum])
            count += 1

    return drugs, placebos

# 5-----------------------------------------------------------------------------------------------------------------------------


def license_test(correct_answers, student_answers):
    """
    ----------------------------------------------------------------------------
    Determines if a student passes a multiple choice driver licence test.
    The function compares a student's answers to the correct answers
    and returns:
        - total number of correctly answered questions
        - total number of incorrectly answered questions
        - a list of the indexes of the incorrectly answered questions
    Use: correct, incorrect, list_incorrect = license_test(correct_answers, student_answers)
    --------------------------------------------------------------------------------
    Parameters:
        correct_answers - list of correct answers (list of ?)
        student_answers - list of student answers (list of ?)
            len(correct_answers) = len(student_answers)
    Returns:
        correct - total number of correctly answered questions (int)
        incorrect - total number of incorrectly answered questions (int)
        list_incorrect - list of indexes of incorrectly answered questions (list of int)
    -------------------------------------------------------

    """
    correct = 0
    incorrect = 0
    list_incorrect = []

    for i in range(len(correct_answers)):
        if correct_answers[i] == student_answers[i]:
            correct += 1
        else:
            incorrect += 1
            list_incorrect.append(i)

    return correct, incorrect, list_incorrect


# 6-----------------------------------------------------------------------------------------------------

def categorize_accidents(city_counts):
    """
    -------------------------------------------------------
    Generates a categorized list of accident counts.
    Every year cities provide the province with a count of vehicle accidents
    over the previous year. Accident counts are categorized according to
    the number of accidents that occur in a year. The categories are
    (up to 100, up to 200, up to 300, up to 400, 400+)
    Use: accidents = categorize_accidents(city_counts)
    -------------------------------------------------------
    Parameters:
        city_counts - a list of accident counts by city (list of int)
    Returns:
        accidents - a count of cities per category (list of int)
    -------------------------------------------------------
    """
    accidents = [0, 0, 0, 0, 0]
    count = 0

    while count < len(city_counts):

        if city_counts[count] < CATEGORIES[0]:
            accidents[0] += 1
        elif city_counts[count] < CATEGORIES[1]:
            accidents[1] += 1
        elif city_counts[count] < CATEGORIES[2]:
            accidents[2] += 1
        elif city_counts[count] < CATEGORIES[3]:
            accidents[3] += 1
        else:
            accidents[4] += 1

        count += 1

    return accidents

# 7----------------------------------------------------------------------------------------------


def num_to_text(num):
    """
    -------------------------------------------------------
    Converts numbers to text. Accepts numbers from 1 to 99.
    Use: text = num_to_text(num)
    -------------------------------------------------------
    Parameters:
        num - a number (1 <= int <= 99)
    Returns:
        text - a text version of num (str)
    -------------------------------------------------------
    """
    count = 0
    found = True
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while found == True and count < len(numbers):

        if num < 10:
            if num == numbers[count]:
                text = ONES[count]
                found = False
        elif num < 20 and num != 10:
            if num == (numbers[count] + 10):
                text = TEENS[count]
                found = False

        elif num == (numbers[count] * 10):
            text = TENS[count]
            found = False

        else:
            unit = num - (num // 10) * 10

            num2 = num - unit

            for i in range(len(numbers)):
                if num2 == (numbers[i] * 10):
                    text = TENS[i]

            for i in range(len(numbers)):
                if unit == (numbers[i]):
                    text = text + '-' + ONES[i]

            found = False

        count += 1

    return text
