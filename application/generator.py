from data.data import nested_list_1, nested_list





def non_recursive_generator(lst):
    
    stack = [iter(lst)]
    new = []
    while stack:
        i = stack.pop()
        try:
            while True:
                data = next(i)
                if isinstance(data, list):
                    stack.append(i)
                    i = iter(data)
                else:
                    new.append(data)
        except StopIteration:
            ...
    return new


# for i in non_recursive_generator(nested_list):
#     print(i)
#     print()
    




def recursive_generator(lst):
    for i in lst:
        if isinstance(i, list):
            yield from recursive_generator(i)
        else:
            yield i


# for i in recursive_generator(nested_list_1):
#     print(i)
