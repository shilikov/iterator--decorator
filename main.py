from typing import List
from application.generator import non_recursive_generator, recursive_generator, flat_generator, flat_generator_v2
from application.iterator import MyIterator, FlatIterator, FlatIteratorV2
from data.data import nested_list_0, nested_list_1, my_list_hard, my_list_simple


print("=" * 30)
for i in MyIterator(nested_list_0):
    print(i)
    


print("=" * 30)
for i in non_recursive_generator(nested_list_0):
    print(i)


print("=" * 30)
for i in recursive_generator(nested_list_1):
    print(i)



print('Задача 1')
for item in FlatIterator(my_list_simple):
    print(item)
print('*' * 25)

print('Задача 2')
for item in flat_generator(my_list_simple):
    print(item)
print('*' * 25)

print('Задача 3')
for item in FlatIteratorV2(my_list_hard):
    print(item)
print('*' * 25)

print('Задача 4')
for item in flat_generator_v2(my_list_hard):
    print(item)
print('*' * 25)



# for row in nested_list:
#     for elem in row:
#         print(elem, end = ' ')
#     print()

