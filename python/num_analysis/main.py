def lab2():
    # Чтение
    data = []
    with open('./data/matrix.txt', 'r') as file:
        for line in file:
            data.append([float(x) for x in line.split()])


if __name__ == '__main__':
    try:
        print('Какую лабораторную запустить?\nВарианты (2): ')
        choice = 'lab' + input()
        eval(choice)()
    except NameError:
        print('Не существует такой лабораторной')
