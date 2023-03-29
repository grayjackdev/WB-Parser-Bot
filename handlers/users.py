from loader import dp, logger
from aiogram.types import Message
from keyboards import get_info_markup


@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    text = '''
Привет🥳 Я бот-парсер, который найдет и сформирует список 
товаров из WB в excel в соответствии с твоим запросом и 
геолокацией😊 Нажми на кнопку "Получить инфо"
    '''
    await message.answer(text, reply_markup=get_info_markup)
