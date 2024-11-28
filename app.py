import random

# Создание поля заданного размера
while True:
    try:
        size = int(input('Задай размер поля: '))
    except ValueError:
        print('Ошибка. Нужно целое число')
        continue
    print(size)
    field = [[None for i in range(size)] for i in range(size)]
    break


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


def is_win(field: list[list]) -> bool:
    """Проверка поля на выйгрышную комбинацию"""
    # Проход по строке
    for row in field:
        row_win = [cell for cell in row if cell is not None]
        if len(set(row_win)) == 1 and len(row_win) == size:
            return True
    # Проход по столбцу
    for i in range(size):
        col_win = [field[k][i] for k in range(size) if field[k][i] is not None]
        if len(set(col_win)) == 1 and len(col_win) == size:
            return True
    # Главная диагональ
    gen_diag_win = [field[i][i] for i in range(size) if field[i][i] is not None]
    if len(set(gen_diag_win)) == 1 and len(gen_diag_win) == size:
        return True
    # Побочная диагональ
    rev_diag_win = [field[i][(size-1)-i] for i in range(size) if field[i][(size-1)-i] is not None]
    if len(set(rev_diag_win)) == 1 and len(rev_diag_win) == size:
        return True
    return False


def step(text):
    """Запрос ввода хода игрока"""
    print(f'Твой ход({text}): ', end='')
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
        row = step('строка')
        col = step('столбец')
        if field[row][col] is not None:
            print('Ошибка ячейка уже занята')
            continue
        field[row][col] = label_player
        break
    view_field(field)


def question_player(text, var1, var2):
    """Спрашивает игрока о выбранном символе и кто начинает игру"""
    while True:
        value = input(f'{text}: ')
        if var1 != value != var2:
            print(f'Ошибка. Введи {var1} или {var2}')
            continue
        break
    return value


def player_change(win_text, player, current_player):
    player = 'x' if player == 'o' else 'o'
    current_player = 'c' if current_player == 'h' else 'h'
    win = win_text
    return win


def step_PC(player, current_player):
    print("Ход компьютера")
    while True:
        if current_player == 'c':
            col, row = random.randint(0, size - 1), random.randint(0, size - 1)
            if field[row][col] is not None:
                continue
            field[row][col] = player
            break
        else:
            break


def game():
    is_first = question_player('Будешь ходить первым? [y/n]','y', 'n')
    symb = question_player('Выбери символ [x/o]','x', 'o')
    # while True:
    #     is_first = input('Будешь ходить первым? [y/n]: ')
    #     if 'y' != is_first != 'n':
    #         print('Ошибка. Введи "y" или "n"')
    #         continue
    #     break
    # while True:
    #     symb = input('Выбери символ [x/o]: ')
    #     if 'x' != symb != 'o':
    #         print('Ошибка. Введи "x" или "o"')
    #         continue
    #     break
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
            player_change('человек', player, current_player)
            # player = 'x' if player == 'o' else 'o'
            # current_player = 'c' if current_player == 'h' else 'h'
            # win = 'человек'
        else:
            step_PC(player, current_player)
            view_field(field)
            player_change('компьютер', player, current_player)
            # print("Ход компьютера")
            # while True:
            #     col, row = random.randint(0, size - 1), random.randint(0, size - 1)
            #     if field[row][col] is not None:
            #         continue
            #     field[row][col] = player
            #     break
            # view_field(field)
            # player = 'x' if player == 'o' else 'o'
            # current_player = 'c' if current_player == 'h' else 'h'
            # win = 'компьютер'
    if is_win(field) is True:
        print(f'Выйграл {win}')
    else:
        print('Ничья')


game()
