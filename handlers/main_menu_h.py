# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from fsm_states import FSM_states

from loguru import logger

from aiogram import types, Dispatcher
# from create_bot import DP
from create_bot import BOT
from keyboards import inline_kb_games


# @DP.callback_query_handler(text='krestiki_noliki')
async def callback_button_krestiki_noliki(callback_query: types.CallbackQuery, state: FSMContext):
    await FSM_states.state_main.set()
    await BOT.send_message(callback_query.from_user.id, \
                           'тут будет игра в крестики-нолики')

    logger.info('выбрана игра в крестики-нолики')


# @DP.callback_query_handler(text='ship_war')
async def callback_button_ship_war(callback_query: types.CallbackQuery, state: FSMContext):
    await FSM_states.state_main.set()
    await BOT.send_message(callback_query.from_user.id, \
                           'тут будет игра в морской бой')

    logger.info('выбрана игра в морской бой')


# @DP.callback_query_handler(text='words')
async def callback_button_words(callback_query: types.CallbackQuery, state: FSMContext):
    await FSM_states.state_main.set()
    await BOT.send_message(callback_query.from_user.id, \
                           'тут будет игра в слова')

    logger.info('выбрана игра в слова')


# ответ на запуск бота
# @DP.message_handler(commands=['start'])
async def command_start(message: types.Message, state: FSMContext):
    await FSM_states.state_main.set()
    await BOT.send_message(message.chat.id,\
                           'Приветствую тебя, землянин! Сыграем?',\
                           reply_markup=inline_kb_games)

    logger.info('пользователь ввел команду /start')


# возвращение к выбору игры
# @DP.callback_query_handler(text='main_menu')
async def callback_button_main_menu(callback_query: types.CallbackQuery):
    await FSM_states.state_main.set()
    await BOT.send_message(callback_query.from_user.id,\
                           'Увидимся позже!', reply_markup=inline_kb_games)

    logger.info('пользователь нажал кнопку возврата в меню выбора игры')


# регистрация всех хэндлеров в отдельной ф-ии
# чтобы потом передать именно ее в нужное место
def register_handlers_main(DP: Dispatcher):
    DP.register_message_handler(command_start, commands=['start'])


    DP.register_callback_query_handler(callback_button_krestiki_noliki, text='krestiki_noliki', state=FSM_states.state_main)
    DP.register_callback_query_handler(callback_button_ship_war, text='ship_war', state=FSM_states.state_main)
    DP.register_callback_query_handler(callback_button_words, text='words', state=FSM_states.state_main)


    DP.register_callback_query_handler(callback_button_main_menu, text='main_menu', state='*')
