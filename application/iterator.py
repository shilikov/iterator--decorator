from data.data import nested_list





class MyIterator:

    def __init__(self, colors) -> None:
        self.colors = colors
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i == len(self.colors):
            raise StopIteration
        if isinstance(self.colors, list):
            return self.colors[self.i]


# for i in MyIterator(nested_list):
#     for j in i:
#         print(j)


    
