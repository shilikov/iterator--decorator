from data.data import nested_list





class MyIterator:

    def __init__(self, lst) -> None:
        self.lst = sum(lst, [])
        

    def __iter__(self):
        self.i = -1
        return self
        

    def __next__(self):
        
        self.i += 1
        if self.i == len(self.lst):
            raise StopIteration
        if isinstance(self.lst, list):
            return self.lst[self.i]





    
