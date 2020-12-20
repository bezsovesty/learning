if __name__ == '__main__':
    try:
        print('Какую лабораторную запустить?\nВарианты (2): ')
        choice = 'lab' + input()
        eval(choice)()
    except NameError:
        print('Не существует такой лабораторной')
