from typing import List, Union
from copy import deepcopy


class Matrix:
    def __init__(self, matrix: List[List[Union[float, int]]]):
        self.__matrix = deepcopy(matrix)

    def __getitem__(self, item: Union[List[int], int]) \
            -> Union[List[Union[float, int]], int, float]:

        if isinstance(item, list) and len(item) > 2:
            raise IndexError('Недопустимое количество индексов.')

        if isinstance(item, int):
            if len(self.__matrix[item]) > 1:
                return self.__matrix[item]
            i, j = item, 0
        else:
            i, j = item

        return self.__matrix[i][j]

    def __setitem__(self, item: Union[int, List[int]],
                    value: Union[int, float, List[Union[float, int]]]):
        if isinstance(item, list) and isinstance(value, list):
            raise TypeError('Неправильные типы аргументов')

        if isinstance(item, int) and isinstance(value, list):
            if len(self.__matrix) != len(value):
                raise ValueError('Неправильное количество аргументов.')
            self.__matrix[item] = value

        elif isinstance(item, int):
            if len(self.__matrix) != 1:
                raise IndexError('Недопустимое количество индексов.')
            self.__matrix[item][0] = value

        else:
            if len(item) > 2:
                raise IndexError('Недопустимое количество индексов.')
            i, j = item
            self.__matrix[i][j] = value

    def __len__(self) -> int:
        """Возвращает кол-во столбцов в матрице."""
        return len(self.__matrix)

    def __str__(self) -> str:
        string = ''
        for row in self.__matrix:
            string += '| '
            for num in row:
                if num >= 0.0:
                    string += ' '
                string += ('%.12f' % num) + '  '
            string += '|\n'
        return string

    def is_symmetric(self) -> bool:
        return len(self.__matrix) == len(self.__matrix[0])
