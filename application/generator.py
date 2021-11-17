



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



def flat_generator(my_list):
    for sub_list in my_list:
        for item in sub_list:
            yield item



def flat_generator_v2(multi_list):
    for item in multi_list:
        if isinstance(item, list):
            # если элемент списка оказывается списком то оборачиваем в этот же генратор
            # такой прием называется рекурсия
            for sub_item in flat_generator_v2(item):
                yield sub_item
        else:
            yield item


