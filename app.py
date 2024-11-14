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
    print(view_field(field))


print(f'"Начальное поле" {view_field(field)}')

print(is_win(field), move('X', field))

# if __name__ == "__main__":

# print(field)
