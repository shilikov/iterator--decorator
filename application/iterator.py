from data.data import nested_list





class MyIterator:

    def __init__(self, colors) -> None:
        self.colors = sum(colors, [])
        

    def __iter__(self):
        self.i = -1
        return self
        

    def __next__(self):
        
        self.i += 1
        if self.i == len(self.colors):
            raise StopIteration
        if isinstance(self.colors, list):
            return self.colors[self.i]





    
