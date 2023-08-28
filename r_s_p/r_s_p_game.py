import random


# набор символов
all_items = ['rock', 'scissors', 'paper']
play_flag = True

# комбинации с вариантом победы одного из участников
win_combinations = [['rock', 'scissors'], ['scissors', 'paper'], ['paper', 'rock']]
# 'rock' - 'scissors'
# 'scissors' - 'paper'
# 'paper' - 'rock'


# ход компьютера
# рандомный символ
def computer_move(items: str) -> str:
    comp = random.choice(items)
    # print('Компьютер выбрал:')
    return comp


# выбор победителя на основе комбинаций
def who_win(user: str, comp: str, win_lst: list, items: str) -> str:
    user = user.lower()
    if user == comp:
        # return 'НИЧЬЯ!'
        return ''
    elif (user in win_lst[0]) and (comp in win_lst[0]):
        if user == items[0]:
            # return 'Ты победил!'
            return user
        else:
            #return 'Победа за компьютером. Попробуй снова!'
            return comp

    elif (user in win_lst[1]) and (comp in win_lst[1]):
        if user == items[1]:
            # return 'Ты победил!'
            return user
        else:
            # return 'Победа за компьютером. Попробуй снова!'
            return comp

    elif (user in win_lst[2]) and (comp in win_lst[2]):
        if user == items[2]:
            # return 'Ты победил!'
            return user
        else:
            # return 'Победа за компьютером. Попробуй снова!'
            return comp
    else:
        # return 'НИЧЬЯ!'
        return ''


# вызывает функцию хода компьютера и поиска победителя
def main(user: str, items: str, win_lst: list) -> str:
    comp_move = computer_move(items)
    print(comp_move)
    print('\n==========')
    
    return who_win(user, comp_move, win_lst, items)


if __name__ == '__main__':
    print('Привет! Давай сыграем в игру?\n')
    
    while play_flag:
        play_flag = True
        user_move = input('Выбери:\nКамень - rock, ножницы - scissors, бумага - paper\n').lower()
        
        if user_move in all_items:
            print(main(user_move, all_items, win_combinations))

        else:
            print('\nЧто-то пошло не так')
            continue

        print('==========\n')
        play_flag = int(input('Сыграем еще?\nДа - 1, нет - 0\n'))

    print('\nВстретимся позже!')
