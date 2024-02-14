
from Sorts_List_linked import Sorts
from List_linked import List
lst = List()
a = [3,2,5,4,1,6]

for i in a:
    lst.append(i)

Sorts.selection_sort(lst)

for i in lst:
    print(i)
