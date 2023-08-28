GAME_BOARD = [i for i in range(1,10)]


def draw_game_board(board: list):
    # отрисовывает поле 3х3
    # в каждой клетке поля - цифры от 1 до 9
    
    print ('-------------')
    for i in range(3):
        print (f'| {board[i*3]} | {board[1+(i*3)]} | {board[2+(i*3)]} |')
        print ('-------------')
        

def step_play(token: str, board: list):
    # дает пользователю возможность хода:
    # ввод строки - номер клетки поля
    
    valid = False
    while not valid:
        # player_answer = input(f'Ход {token}\nВведи номер клетки: ')
        
        try:
            player_answer = int(input(f'Ход {token}\nВведи номер клетки: '))
        except:
            print ('Ошибка. Введи число!')
            continue
        
        if 1 <= player_answer <= 9:
            # проверка, что на поле в выбраной клетке нет Х или О
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = token
                valid = True
            else:
                print ('Эта клетка уже занята! Попробуй еще раз.')
        else:
            print ('Ошибка. Введи номер свободной клетки!')


def check_win(board: list):
    # выбор победителя
    # возвращает False, если нет победителя
    # возвращает Х или О, если собрана комбинация
    
    win_combination = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for coord in win_combination:
        if board[coord[0]] == board[coord[1]] == board[coord[2]]:
            # победитель Х иили О
            return board[coord[0]]
    
    return False


def main(board: list):
    # основная функция
    
    step = 0
    win = False
    
    while not win:
        # отрисовка поля
        draw_game_board(board)
        # если ход четный по счету - ходит Х
        # если ход нечетный по счету - ходит О
        if step % 2 == 0:
            step_play('X', board)
        else:
            step_play('O', board)
        step += 1
        
        # с 5 хода от начала игры проверка побдителя
        if step > 4:
            winner = check_win(board)
            #!!!!!!!!!!!!!!!!!!!!!!!!!
            if winner:
                print (f'В этот раз {winner} победили!')
                win = True
                break
        
        # если поле заполнено
        if step == 9:
            print ('Ничья!')
            break
    
    draw_game_board(board)


if __name__ == '__main__':
    main(GAME_BOARD)