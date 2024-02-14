"""
-------------------------------------------------------
Assignment 9, Task 5
-------------------------------------------------------
"""
from functions import student_info

file = input('Input file: ')
students = open('{}'.format(file), 'r')
print()

l_id, h_id, avg = student_info(students)
students.close()

print('ID of lowest mark: {}'.format(l_id))
print('ID of highest mark: {}'.format(h_id))
print('Average: {:.2f}'.format(avg))
