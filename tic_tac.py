from itertools import chain

area = []

save = {'X': 0, '0': 0}

def clear_area():
    area.clear()

def draw_area():
    for i in area:
        print(*i)

def save_score(chars):
    save[chars] += 1


def check_turn_chars(row, col):
    cur_char = area[row][col]

    if cur_char != '*':
        check = 0
    else:
        check = 1

    return check


def check_horizontal_line(turn_chars):
    flag = 0
    for i in area:
        size = len(i)
        cnt = i.count(turn_chars)

        if cnt == size:
            flag = 1
            return flag

    return flag


def check_vertical_line(turn_chars):
    flag = 0
    cnt = 0
    size = len(area)
    for i in range(size):
        for k in range(size):
            value = area[k][i]
            if value == turn_chars:
                cnt += 1

            if cnt == size:
                flag = 1

            if flag == 1:
                return flag

            if k == size - 1:
                cnt = 0

    return flag


def check_diagonal_line(turn_chars):
    cnt = 0
    flag = 0
    size = len(area)
    for i in range(size):
        value = area[i][i]
        if value == turn_chars:
            cnt += 1

        if cnt == size:
            flag = 1

        if flag == 1:
            return flag

    l = 0
    cnt = 0
    for k in reversed(range(size)):
        value = area[k][l]

        if value == turn_chars:
            cnt += 1

        if cnt == size:
            flag = 1
        if flag == 1:
            return flag

        l += 1

    return flag


def check_winner(turn_chars):
    chl = check_horizontal_line(turn_chars)
    if chl == 1:
        print('Победа по горизонтали')
        return 1

    cvl = check_vertical_line(turn_chars)
    if cvl == 1:
        print('Победа по вертикали')
        return 1

    cdl = check_diagonal_line(turn_chars)
    if cdl == 1:
        print('Победа по диагонали')
        return 1

    return 0


def start_game():
    clear_area()
    if sum(save.values()) == 0:
        print('Добро пожаловать в игру крестики-нолики')
        print()

    print(f'Крестики - {save['X']}   Нолики - {save['0']}')
    print()
    size = int(input('Введите размер сетки (2-5): '))

    for i in range(size):
        area.append([])
        for j in range(size):
            area[i].append('*')

    print()
    print('Игра началась')

    k = 1

    while k < len(list(chain(*area))) + 1:
        print()

        draw_area()

        print()

        print(f'Ход № {k}')

        if k % 2 == 0:
            print('Сейчас ход ноликов')
            turn_chars = '0'
        else:
            print('Сейчас ход крестиков')
            turn_chars = 'X'

        row = int(input('Введите номер строки: ')) - 1
        col = int(input('Введите номер колонки: ')) - 1

        print()

        if check_turn_chars(row, col) == 0:
            print('Ячейка занята')
            continue

        area[row][col] = turn_chars


        if check_winner(turn_chars) == 1:
            print()
            if turn_chars == 'X':
                winner = 'крестики'
            else:
                winner = 'нолики'

            draw_area()
            print()
            print('Игра окончена, победили ' + winner)
            save_score(turn_chars)
            print()

            retry = input('Хотите начать новую игру? (y/n): ')

            print()

            if retry == 'y':
                start_game()
            else:
                break


        k += 1



start_game()
