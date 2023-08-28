# from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


# создание кнопок с callback_data
inline_btn_coin_toss = InlineKeyboardButton('Подбросить!', callback_data='coin_toss')
inline_btn_main_menu = InlineKeyboardButton('Вернуться к выбору игры', callback_data='main_menu')


# запись кнопок в клавиатуру
inline_kb_coin_toss = InlineKeyboardMarkup().add(inline_btn_coin_toss, inline_btn_main_menu)
