cell = None
size = 3
field = [[cell] * size] * size
# count_cell = list(range(1, size+1))

def is_win(field: list[list]):
    # Проход по строке
    for row in field:
        if row[0] == row[1] == row[2] and row[0]:
            return True
    # Проход по столбцу
    for i in range(size):
        if field[0][i] == field[1][i] == field[2][i] and field[0][i]:
            return True
    # Главаная диагональ
    if field[0][0] == field[1][1] == field[2][2] and field[0][0]:
        return True
    # Побочная диагональ
    if field[0][2] == field[1][1] == field[2][0] and field[0][2]:
        return True
    return False

def move(label_player, field):
    step_line = input('В какую ячейку строки будет ход?')
    def
    step_column = input('В какую ячейку столбца будет ход?')




    if field[step_line][step_column]