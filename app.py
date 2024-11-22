import random

# Создание поля заданного размера
size = int(input('Задай размер поля: '))
print(size)
field = []
for i in range(size):
    line = []
    for i in range(size):
        line.append(None)
    field.append(line)


# field = [[None, None, None], [None, None, None], [None, None, None]]
# size = 3


def view_field(field: list[list]) -> print:
    """ Выводит размеченное игровое поле в столбец """
    for row in field:
        print('|', end='')
        for cell in row:
            if cell is None:
                print(' |', end='')
            else:
                print(f'{cell}|', end='')
        print()


# def is_win(field: list[list]) -> bool:
#     """Проверка поля на выйгрышную комбинацию"""
#     # Проход по строке
#     for row in field:
#         if row[0] == row[1] == row[2] and row[0]:
#             return True
#     # Проход по столбцу
#     for i in range(3):
#         if field[0][i] == field[1][i] == field[2][i] and field[0][i]:
#             return True
#     # Главная диагональ
#     if field[0][0] == field[1][1] == field[2][2] and field[0][0]:
#         return True
#     # Побочная диагональ
#     if field[0][2] == field[1][1] == field[2][0] and field[0][2]:
#         return True
#     return False

def is_win(field: list[list]) -> bool:
    """Проверка поля на выйгрышную комбинацию"""
    # Проход по строке
    # if row[0] == row[1] == row[2] and row[0]:
    for row in field:
        row_win = []
        for cell in row:
            if cell is not None:
                row_win.append(cell)
        if len(set(row_win)) == 1 and len(row_win) == size:
            return True
    # Проход по столбцу
    # if field[0][i] == field[1][i] == field[2][i] and field[0][i]:
    for i in range(size):
        col_win = []
        for k in range(size):
            if field[k][i] is not None:
                col_win.append(field[k][i])
        if len(set(col_win)) == 1 and len(col_win) == size:
            return True
    # Главная диагональ
    # if field[0][0] == field[1][1] == field[2][2] and field[0][0]:
    gen_diag_win = []
    for i in range(size):
        if field[i][i] is not None:
            gen_diag_win.append(field[i][i])
    if len(set(gen_diag_win)) == 1 and len(gen_diag_win) == size:
        return True
    # Побочная диагональ
    # if field[0][2] == field[1][1] == field[2][0] and field[0][2]:
    rev_diag_win = []
    for i in range(size):
        if field[i][(size-1)-i] is not None:
            rev_diag_win.append(field[i][(size-1)-i])
    if len(set(rev_diag_win)) == 1 and len(rev_diag_win) == size:
        return True
    return False


# def move(label_player: str, field: list[list]) -> print:
#     """Ход пользователя и вывод измененного игрового поля"""
#     while True:
#         # Заменить на функцию
#         while True:
#             try:
#                 row = int(input('Твой ход(строка): '))
#                 row -= 1
#             except ValueError:
#                 print('Ошибка. Нужно целое число')
#                 continue
#             if not 0 <= row <= size - 1:
#                 print('Ошибка. Неверный диапазон')
#                 continue
#             break
#         while True:
#             try:
#                 col = int(input('Твой ход(столбец): '))
#                 col -= 1
#             except ValueError:
#                 print('Ошибка. Нужно целое число')
#                 continue
#             if not 0 <= col <= size - 1:
#                 print('Ошибка неверный диапазон')
#                 continue
#             break
#         if field[row][col] is not None:
#             print('Ошибка ячейка уже занята')
#             continue
#         field[row][col] = label_player
#         break
#     view_field(field)

def step():
    """Запрос ввода хода игрока"""
    while True:
        try:
            value = int(input())
            value -= 1
        except ValueError:
            print('Ошибка. Нужно целое число')
            continue
        if not 0 <= value <= size - 1:
            print('Ошибка. Неверный диапазон')
            continue
        return value


def move(label_player: str, field: list[list]) -> print:
    """Ход пользователя и вывод измененного игрового поля"""
    while True:
        print('Твой ход(строка):', end='')
        row = step()
        print('Твой ход(столбец):', end='')
        col = step()
        if field[row][col] is not None:
            print('Ошибка ячейка уже занята')
            continue
        field[row][col] = label_player
        break
    view_field(field)


def game():
    while True:
        is_first = input('Будешь ходить первым? [y/n]: ')
        if 'y' != is_first != 'n':
            print('Ошибка. Введи "y" или "n"')
            continue
        break
    while True:
        symb = input('Выбери символ [x/o]: ')
        if 'x' != symb != 'o':
            print('Ошибка. Введи "x" или "o"')
            continue
        break
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

    count_step = 0
    while not is_win(field) and 0 <= count_step < size * size:
        count_step += 1
        if current_player == 'h':
            move(player, field)
            player = 'x' if player == 'o' else 'o'
            current_player = 'c' if current_player == 'h' else 'h'
            win = 'человек'
        else:
            print("Ход компьютера")
            while True:
                col, row = random.randint(0, size - 1), random.randint(0, size - 1)
                if field[row][col] is not None:
                    continue
                field[row][col] = player
                break
            view_field(field)
            player = 'x' if player == 'o' else 'o'
            current_player = 'c' if current_player == 'h' else 'h'
            win = 'компьютер'
    if is_win(field) is True:
        print(f'Выйграл {win}')
    else:
        print('Ничья')


game()