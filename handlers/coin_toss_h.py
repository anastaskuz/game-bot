from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from loguru import logger

from fsm_states import FSM_states
from create_bot import BOT
from keyboards import inline_kb_coin_toss
from monetka import coin_toss


# ответ на кнопку игры монетка
# @DP.callback_query_handler(text='monetka', state=state_main)
async def callback_button_monetka(callback_query: types.CallbackQuery, state: FSMContext):
    await FSM_states.state_monetka.set()
    await BOT.send_message(callback_query.from_user.id, \
                           'Тык на кнопку - бросок монетки', reply_markup=inline_kb_coin_toss)

    logger.info('пользователь выбрал игру в монетку')


# @DP.callback_query_handler(text='coin_toss', state=state_monetka)
async def callback_button_coin_toss(callback_query: types.CallbackQuery, state: FSMContext):
    await FSM_states.state_monetka.set()
    result = coin_toss.coin_toss()
    await BOT.send_message(callback_query.from_user.id, \
                           f'Иииии выпадает...\n{result}', reply_markup=inline_kb_coin_toss)

    logger.info('пользователь подбросил монетку')


# регистрация всех хэндлеров в отдельной ф-ии
# чтобы потом передать именно ее в нужное место
def register_handlers_coin_toss(DP: Dispatcher):
    DP.register_callback_query_handler(callback_button_monetka, text='monetka', state=FSM_states.state_main)
    DP.register_callback_query_handler(callback_button_coin_toss, text='coin_toss', state=FSM_states.state_monetka)
