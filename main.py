from typing import List
from application.generator import non_recursive_generator, recursive_generator
from application.iterator import MyIterator
from data.data import nested_list, nested_list_1


print("=" * 30)
for i in MyIterator(nested_list_1):
    print(i)
    


print("=" * 30)
for i in non_recursive_generator(nested_list):
    print(i)


print("=" * 30)
for i in recursive_generator(nested_list_1):
    print(i)


# for row in nested_list:
#     for elem in row:
#         print(elem, end = ' ')
#     print()

