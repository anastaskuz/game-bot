from aiogram.dispatcher.filters.state import State, StatesGroup


class FSM_states(StatesGroup):
    # основное
    state_main = State()
    # выбор количества игроков (1 или 2)
    state_how_users = State()


    # monetka
    state_monetka = State()


    # r_s_p
    # ход игрока при игре с компьютером
    state_user_move = State()
    # ход первого игрока
    state_user1_move = State()
    # ход второго игрока
    state_user2_move = State()
    # предложение сыграть снова или выйти из игры
    state_finish = State()

    
    # lristiki_noliki
    
    # review
    state_review = State()