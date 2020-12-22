from .Matrix import Matrix
from typing import List, Union


class Slay:
    def __init__(self, matrix: List[List[Union[float, int]]],
                 vector: List[List[Union[float, int]]]):
        self.matrix = Matrix(matrix)
        self.vector = Matrix(vector)

    def __len__(self) -> int:
        return len(self.matrix)

    def __str__(self) -> str:
        str_matrix = self.matrix.__str__()
        str_vector = self.vector.__str__()

        # Форматирование
        pos = int(str_matrix.index('\n') / 2) - 3
        head = ' ' * pos + 'MATRIX' + (' ' * (pos + 10)) + 'VECTOR\n'

        # Разбиение строк на массив
        str_matrix = str_matrix.split('\n')
        str_vector = str_vector.split('\n')

        string = ''
        for i in range(len(str_matrix)):
            string += str_matrix[i] + '   ' + str_vector[i] + '\n'

        return head + string
