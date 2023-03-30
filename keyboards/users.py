from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

get_info_markup = ReplyKeyboardMarkup([
    [
        KeyboardButton('ℹ️Получить инфо')
    ]
], resize_keyboard=True)

cancel_markup = ReplyKeyboardMarkup([
    [
        KeyboardButton('📛Отмена')
    ]
], resize_keyboard=True)

