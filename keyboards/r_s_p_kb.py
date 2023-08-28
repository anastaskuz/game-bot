# from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


# создание кнопок с callback_data
inline_btn_rule = InlineKeyboardButton('Прочитать правила', callback_data='rule')
inline_btn_error = InlineKeyboardButton('Сообщить об ошибке', callback_data='error')
inline_btn_exit = InlineKeyboardButton('Вернуться к выбору количества игроков', callback_data='exit')
inline_btn_main_menu = InlineKeyboardButton('Вернуться к выбору игры', callback_data='main_menu')


inline_btn_one_user = InlineKeyboardButton('С компьютером', callback_data='one')
inline_btn_two_user = InlineKeyboardButton('С другом', callback_data='two')
inline_btn_rock = InlineKeyboardButton('Камень', callback_data='rock')
inline_btn_scissors = InlineKeyboardButton('Ножницы', callback_data='scissors')
inline_btn_paper = InlineKeyboardButton('Бумага', callback_data='paper')


# запись кнопок в клавиатуру
inline_kb_rule = InlineKeyboardMarkup().add(inline_btn_rule, inline_btn_error)
inline_kb_play = InlineKeyboardMarkup().add(inline_btn_rock, inline_btn_scissors, inline_btn_paper, inline_btn_exit, inline_btn_main_menu)
inline_kb_how_users = InlineKeyboardMarkup().add(inline_btn_one_user, inline_btn_two_user, inline_btn_main_menu)
