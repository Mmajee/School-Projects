"""
-------------------------------------------------------
Assignment 8, Task 4
-------------------------------------------------------
"""
from functions import set_trials

subjects = ['David', 'Tasmin', 'Tristan', 'Lori', 'Kate', 'Li-Meng']
print('Subjects: {}'.format(subjects))

drugs, placebos = set_trials(subjects)

print('Drug trial: {}'.format(drugs))
print('Placebo trial: {}'.format(placebos))
