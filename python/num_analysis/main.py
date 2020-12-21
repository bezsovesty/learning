from NumAnalysis import *


def lab2():
    # Чтение
    data = []
    with open('./data/matrix.txt', 'r') as file:
        for line in file:
            data.append([float(x) for x in line.split()])

    # Удаление последнего элемента в каждой строке
    #   чтобы образовать свободный вектор.
    vector = []
    for row in data:
        elem = row.pop()
        vector.append([elem])

    slay = Slay(data, vector)
    print('Прочитанная матрица:\n', slay)


if __name__ == '__main__':
    try:
        print('Какую лабораторную запустить?\nВарианты (2): ')
        choice = 'lab' + input()
        eval(choice)()
    except NameError:
        print('Не существует такой лабораторной')
