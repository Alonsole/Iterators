"""Необязательное задание. Написать итератор, аналогичный итератору из задания 1, но
обрабатывающий списки с любым уровнем вложенности. Шаблон и тест в коде ниже:"""


class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.new_list = []
        self.index = 0
        self.flat(self.list_of_list)

    def flat(self, lst):
        for item in lst:
            self.flat(item) if isinstance(item, list) else self.new_list.append(item)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.new_list):
            item = self.new_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
