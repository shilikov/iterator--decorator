





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





class FlatIterator:

    def __init__(self, multi_list):

        self.multi_list = multi_list  # список с воложенными списками

    def __iter__(self):
        self.multi_list_iter = iter(self.multi_list)
        self.nested_list = []  # вложенный список с элементами
        self.nested_list_cursor = -1
        return self

    def __next__(self):
        self.nested_list_cursor += 1
        if len(self.nested_list) == self.nested_list_cursor:
            self.nested_list = None
            self.nested_list_cursor = 0
            while not self.nested_list:
                self.nested_list = next(self.multi_list_iter)
                #  если  список список пустой, то получаем селдующий
                #  если списки закончаться, получим stop iteration

        return self.nested_list[self.nested_list_cursor]




class FlatIteratorV2:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        self.iterators_queue = []  # очередь
        self.current_iterator = iter(self.multi_list)
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iterator)
                #  пытаемся получить следующий элемент
            except StopIteration:
                if not self.iterators_queue:
                    # если в текущем итераторе элементов не осталось и очередь иетраторов пуста
                    # завершаем цикл
                    raise StopIteration
                else:
                    # берем итератор из очереди
                    self.current_iterator = self.iterators_queue.pop()
                    continue
            if isinstance(self.current_element, list):
                # если следующий эелемент оказался списком, то
                # добавляем текущий итератор в очередь
                # а текущим итераторм делаем следующий элемент
                self.iterators_queue.append(self.current_iterator)
                self.current_iterator = iter(self.current_element)
            else:
                # если элемент не список, то прщсто возвращаем его
                return self.current_element

