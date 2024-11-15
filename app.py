import random

# Создание и вывод поля заданного размера
# size = int(input('Задай размер поля: '))
# print(size)
# field = []
# for i in range(size):
#     line = []
#     for i in range(size):
#         line.append(None)
#     field.append(line)
#
# print("Начальное поле")
# for row in field:
#     print('|', end='')
#     for cell in row:
#         if cell is None:
#             print(' |', end='')
#         else:
#             print(f'{cell}', end='')
#     print()


field = [[None, None, None], [None, None, None], [None, None, None]]
size = 3


def view_field(field: list[list]):
    """ Выводит размеченное игровое поле в столбец """
    for row in field:
        print('|', end='')
        for cell in row:
            if cell is None:
                print(' |', end='')
            else:
                print(f'{cell}|', end='')
        print()


def is_win(field: list[list]):
    """Проверка поля на выйгрышную комбинацию"""
    # Проход по строке
    for row in field:
        if row[0] == row[1] == row[2] and row[0]:
            return True
    # Проход по столбцу
    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] and field[0][i]:
            return True
    # Главная диагональ
    if field[0][0] == field[1][1] == field[2][2] and field[0][0]:
        return True
    # Побочная диагональ
    if field[0][2] == field[1][1] == field[2][0] and field[0][2]:
        return True
    return False


def move(label_player, field):
    """Ход пользователя и вывод измененного игрового поля"""
    while True:
        # Заменить на функцию
        while True:
            try:
                row = int(input('Твой ход(строка): '))
                row -= 1
            except ValueError:
                print('Ошибка. Нужно целое число')
                continue
            if not 0 <= row <= size - 1:
                print('Ошибка. Неверный диапазон')
                continue
            break
        while True:
            try:
                col = int(input('Твой ход(столбец): '))
                col -= 1
            except ValueError:
                print('Ошибка. Нужно целое число')
                continue
            if not 0 <= col <= size - 1:
                print('Ошибка неверный диапазон')
                continue
            break
        if field[row][col] is not None:
            print('Ошибка ячейка уже занята')
            continue
        field[row][col] = label_player
        break
    view_field(field)

def game():
    is_first = input('Будешь ходить первым? [y/n]: ')
    symb = input('Выбери символ [x/o]: ')
    current_player = None
    win = None

    if is_first == 'y':
        player = symb
        current_player = 'h'
    else:
        player = 'x' if symb == 'o' else 'o'
        current_player = 'c'

    print(f'"Начальное поле"')
    view_field(field)

    # if is_win(field) is False:
    #     while is_win(field) is False:
    #         if current_player == 'h':
    #             move(player, field)
    #             player = 'x' if player == 'o' else 'o'
    #             current_player = 'c' if current_player == 'h' else 'h'
    #             win = 'h'
    #         else:
    #             print("Ходит компьютер")
    #             while True:
    #                 col, row = random.randint(0, size-1), random.randint(0, size-1)
    #                 if field[row][col] is not None:
    #                     continue
    #                 field[row][col] = player
    #                 break
    #             view_field(field)
    #             player = 'x' if player == 'o' else 'o'
    #             current_player = 'c' if current_player == 'h' else 'h'
    #             win = 'c'
    # else:
    #     print(f'Выйграл игрок {win}')

    while not is_win(field):
        if current_player == 'h':
            move(player, field)
            player = 'x' if player == 'o' else 'o'
            current_player = 'c' if current_player == 'h' else 'h'
            win = 'h'
        else:
            print("Ходит компьютер")
            while True:
                col, row = random.randint(0, size-1), random.randint(0, size-1)
                if field[row][col] is not None:
                    continue
                field[row][col] = player
                break
            view_field(field)
            player = 'x' if player == 'o' else 'o'
            current_player = 'c' if current_player == 'h' else 'h'
            win = 'c'
    print(f'Выйграл игрок {win}')






game()
