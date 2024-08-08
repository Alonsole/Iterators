"""Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает
список списков и возвращает их плоское представление, т. е. последовательность, состоящую из
вложенных элементов. Функция test в коде ниже также должна отработать без ошибок."""


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        self.cursor = -1  
        self.list_len = len(self.list_of_lists)

    def __iter__(self):
        self.cursor += 1
        self.list_cursor = 0
        return self

    def __next__(self):
        while self.cursor - self.list_len and self.list_cursor == len(self.list_of_lists[self.cursor]):
            iter(self)
        if self.cursor == self.list_len:
            raise StopIteration
        self.list_cursor += 1
        item = self.list_of_lists[self.cursor][self.list_cursor - 1]
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
