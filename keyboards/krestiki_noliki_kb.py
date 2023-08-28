from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


# создание кнопок с callback_data
inline_btn_exit = InlineKeyboardButton('Вернуться к выбору количества игроков', callback_data='exit')
inline_btn_main_menu = InlineKeyboardButton('Вернуться к выбору игры', callback_data='main_menu')


# запись кнопок в клавиатуру
inline_kb_rule = InlineKeyboardMarkup().add(inline_btn_rule, inline_btn_error)
