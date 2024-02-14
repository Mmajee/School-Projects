"""
-------------------------------------------------------
Assignment 8, Task 5
-------------------------------------------------------
"""
from functions import license_test

correct_answers = [1, 1, 3, 4, 2, 2, 1, 3, 4, 3]
print(correct_answers)
student_answers = [1, 1, 3, 4, 2, 2, 1, 3, 4, 3]
print(student_answers)

correct, incorrect, list_incorrect = license_test(
    correct_answers, student_answers)

print('Correct Answers Count: {}'.format(correct))
print('Incorrect Answers Count: {}'.format(incorrect))
print('Indexes of incorrect answers: {}'.format(list_incorrect))
