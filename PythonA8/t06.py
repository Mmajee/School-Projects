"""
-------------------------------------------------------
Assignment 8, Task 6
-------------------------------------------------------
"""
from functions import categorize_accidents

city_counts = [387, 306, 126, 154, 354, 244, 172, 504, 205,
               412, 274, 555, 406, 127, 42, 331, 534, 576, 64, 219]
print('City Accident Counts: {}'.format(city_counts))

accidents = categorize_accidents(city_counts)

print('Accidents Categorized: {}'.format(accidents))
print()
print('Category  Counts')
print('< 100 {:>10d}'.format(accidents[0]))
print('< 200 {:>10d}'.format(accidents[1]))
print('< 300 {:>10d}'.format(accidents[2]))
print('< 400 {:>10d}'.format(accidents[3]))
print('400 or more {:>4d}'.format(accidents[4]))
