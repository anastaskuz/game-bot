# from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


# создание кнопок с callback_data
inline_btn_help = InlineKeyboardButton('Подсказка', callback_data='help')

inline_btn_krestiki_noliki = InlineKeyboardButton('Крестики-Нолики', callback_data='krestiki_noliki')
inline_btn_r_s_p = InlineKeyboardButton('Камень-Ножницы-Бумага', callback_data='r_s_p')
inline_btn_monetka = InlineKeyboardButton('Подбрось монетку', callback_data='monetka')
inline_btn_ship_war = InlineKeyboardButton('Морской бой', callback_data='ship_war')
inline_btn_words = InlineKeyboardButton('Слова', callback_data='words')


# запись кнопок в клавиатуру
inline_kb_help = InlineKeyboardMarkup().add(inline_btn_help)
inline_kb_games = InlineKeyboardMarkup().add(inline_btn_krestiki_noliki, \
                                             inline_btn_r_s_p, \
                                             inline_btn_monetka, \
                                             inline_btn_ship_war, \
                                             inline_btn_words)
