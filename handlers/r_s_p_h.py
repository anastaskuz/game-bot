# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher


from create_bot import BOT
# from create_bot import DP
# from keyboards import inline_kb_rule
from keyboards import inline_kb_play
# from keyboards import inline_kb_y_or_n
from keyboards import inline_kb_how_users

from fsm_states import FSM_states
from r_s_p import r_s_p_game


all_items = r_s_p_game.all_items
win_combinations = r_s_p_game.win_combinations


async def step_user_vs_comp(callback_query = types.CallbackQuery, state = FSMContext):
    await FSM_states.state_finish.set()
    user_move = str(callback_query.data)
    # тут будет функция рандомного выбора к н б
    comp_move = r_s_p_game.computer_move(all_items)
    # тут будет "имя" победителя
    winner = r_s_p_game.who_win(user_move, comp_move, win_combinations, all_items)

    await BOT.send_message(callback_query.from_user.id, \
                           f'Ты выбрал: {user_move} \nVS\nКомпьютер выбрал: {comp_move}')
    if winner == user_move:
        await BOT.send_message(callback_query.from_user.id, \
                           f'Ты победил!')
    elif winner == comp_move:
        await BOT.send_message(callback_query.from_user.id, \
                           f'Победил компьютер!')
    elif winner == '':
        await BOT.send_message(callback_query.from_user.id, \
                           f'НИЧЬЯ!')
    else:
        await BOT.send_message(callback_query.from_user.id, \
                           f'Error')

    await FSM_states.state_user_move.set()
    await BOT.send_message(callback_query.from_user.id, \
                           'Сделай свой ход', reply_markup=inline_kb_play)


async def step_user1(callback_query = types.CallbackQuery, state = FSMContext):
    # запись значения в хранилище состояния
    await state.update_data(user1_move = str(callback_query.data))
    await FSM_states.state_user2_move.set()
    await BOT.send_message(callback_query.from_user.id, \
                           'Ход игрока номер 2', reply_markup=inline_kb_play)


async def step_user2(callback_query = types.CallbackQuery, state = FSMContext):
    user2_move = str(callback_query.data)
    await FSM_states.state_finish.set()

    # тут будет "имя" победителя
    data_move = await state.get_data()
    winner = r_s_p_game.who_win(user1_move := data_move.get('user1_move'), user2_move, win_combinations, all_items)

    await BOT.send_message(callback_query.from_user.id, \
                           f'Выбрал игрок 1: {user1_move} \nVS\nВыбрал игрок 2: {user2_move}')
    if winner == user1_move:
        await BOT.send_message(callback_query.from_user.id, \
                           f'Победил игрок 1!')
    elif winner == user2_move:
        await BOT.send_message(callback_query.from_user.id, \
                           f'Победил игрок 2!')
    elif winner == '':
        await BOT.send_message(callback_query.from_user.id, \
                           f'НИЧЬЯ!')

    await FSM_states.state_user1_move.set()
    await BOT.send_message(callback_query.from_user.id, \
                           'Ход игрока номер 1', reply_markup=inline_kb_play)


# кнопка правил
# @DP.callback_query_handler(text='rule', state=state_main)
async def callback_button_rule(callback_query: types.CallbackQuery, state: FSMContext):
    await BOT.send_message(callback_query.from_user.id, \
                           'Тут будут правила игры')


######################################################################################

# ответ на кнопку игры в кнб
# @DP.callback_query_handler(text='r_s_p', state=state_main)
async def callback_button_r_s_p(callback_query: types.CallbackQuery, state: FSMContext):
    # ввод в состояние выбора количества игроков
    await FSM_states.state_how_users.set()
    await BOT.send_message(callback_query.from_user.id, \
                           'Игра с компьютером или с другом?', reply_markup=inline_kb_how_users)


######################################################################################


# ход игрока при выборе игры с компьютером
# @DP.callback_query_handler(text='one', state=state_how_users)
async def callback_button_one(callback_query: types.CallbackQuery, state: FSMContext):
    await FSM_states.state_user_move.set()
    await BOT.send_message(callback_query.from_user.id, \
                           'Сделай свой ход', reply_markup=inline_kb_play)


# выбор игроком камня (игра с компьютером)
# @DP.callback_query_handler(text='rock', state=state_user_move)
async def callback_button_rock_user(callback_query: types.CallbackQuery, state: FSMContext):
    await step_user_vs_comp()


# выбор игроком ножниц (игра с компьютером)
# @DP.callback_query_handler(text='scissors', state=state_user_move)
async def callback_button_scissors_user(callback_query: types.CallbackQuery, state: FSMContext):
    await step_user_vs_comp()


# выбор игроком бумаги (игра с компьютером)
# @DP.callback_query_handler(text='paper', state=state_user_move)
async def callback_button_paper_user(callback_query: types.CallbackQuery, state: FSMContext):
    await step_user_vs_comp()


######################################################################################

# ход первого игрока (игра вдвоем)
# @DP.callback_query_handler(text='two', state=state_how_users)
async def callback_button_two(callback_query: types.CallbackQuery, state: FSMContext):
    await FSM_states.state_user1_move.set()
    await BOT.send_message(callback_query.from_user.id, \
                           'Ход игрока номер 1', reply_markup=inline_kb_play)


# выбор первым игроком камня (игра вдвоем)
# @DP.callback_query_handler(text='rock', state=state_user1_move)
async def callback_button_rock_user1(callback_query: types.CallbackQuery, state: FSMContext):
    await step_user1()


# выбор первым игроком ножниц (игра вдвоем)
# @DP.callback_query_handler(text='scissors', state=state_user1_move)
async def callback_button_scissors_user1(callback_query: types.CallbackQuery, state: FSMContext):
    await step_user1()


# выбор первым игроком бумаги (игра вдвоем)
# @DP.callback_query_handler(text='paper', state=state_user1_move)
async def callback_button_paper_user1(callback_query: types.CallbackQuery, state: FSMContext):
    await step_user1()


# выбор вторым игроком камня (игра вдвоем)
# @DP.callback_query_handler(text='rock', state=state_user2_move)
async def callback_button_rock_user2(callback_query: types.CallbackQuery, state: FSMContext):
    await step_user2()


# выбор вторым игроком ножниц (игра вдвоем)
# @DP.callback_query_handler(text='scissors', state=state_user2_move)
async def callback_button_scissors_user2(callback_query: types.CallbackQuery, state: FSMContext):
    await step_user2()


# выбор вторым игроком бумаги (игра вдвоем)
# @DP.callback_query_handler(text='paper', state=state_user2_move)
async def callback_button_paper_user2(callback_query: types.CallbackQuery, state: FSMContext):
    await step_user2()


######################################################################################


# выбор продолжения игры
# @DP.callback_query_handler(text='exit')
async def callback_button_exit(callback_query: types.CallbackQuery, state: FSMContext):
    await FSM_states.state_how_users.set()
    await BOT.send_message(callback_query.from_user.id, \
                           'Сколько игроков?', reply_markup=inline_kb_how_users)


######################################################################################


# регистрация всех хэндлеров в отдельной ф-ии
# чтобы потом передать именно ее в нужное место
def register_handlers_r_s_p(DP: Dispatcher):
    DP.register_callback_query_handler(callback_button_r_s_p, text='r_s_p', state=FSM_states.state_main)
    DP.register_callback_query_handler(callback_button_rule, text='rule', state=FSM_states.state_main)


    DP.register_callback_query_handler(callback_button_one, text='one', state=FSM_states.state_how_users)
    DP.register_callback_query_handler(callback_button_rock_user, text='rock', state=FSM_states.state_user_move)
    DP.register_callback_query_handler(callback_button_scissors_user, text='scissors', state=FSM_states.state_user_move)
    DP.register_callback_query_handler(callback_button_paper_user, text='paper', state=FSM_states.state_user_move)


    DP.register_callback_query_handler(callback_button_two, text='two', state=FSM_states.state_how_users)
    DP.register_callback_query_handler(callback_button_rock_user1, text='rock', state=FSM_states.state_user1_move)
    DP.register_callback_query_handler(callback_button_scissors_user1, text='scissors', state=FSM_states.state_user1_move)
    DP.register_callback_query_handler(callback_button_paper_user1, text='paper', state=FSM_states.state_user1_move)

    DP.register_callback_query_handler(callback_button_rock_user2, text='rock', state=FSM_states.state_user2_move)
    DP.register_callback_query_handler(callback_button_scissors_user2, text='scissors', state=FSM_states.state_user2_move)
    DP.register_callback_query_handler(callback_button_paper_user2, text='paper', state=FSM_states.state_user2_move)


    DP.register_callback_query_handler(callback_button_exit, text='exit', state='*')
