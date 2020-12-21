from typing import List, Union
from copy import deepcopy


class Matrix:
    def __init__(self, matrix: List[List[Union[float, int]]]):
        self.__matrix = deepcopy(matrix)

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

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
