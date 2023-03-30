from aiogram.dispatcher import FSMContext
from loader import dp, logger
from aiogram.types import Message
from keyboards import get_info_markup, cancel_markup
from utils import get_addr, Wildberries
from filters import IsNumber


@dp.message_handler(commands=['start'], state='*')
async def start_command(message: Message, state: FSMContext):
    await state.reset_state()
    text = '''
Привет🥳 Я бот-парсер, который найдет и сформирует список 
товаров из WB в excel в соответствии с твоим запросом и 
геолокацией😊 Нажми на кнопку "Получить инфо"
    '''
    await message.answer(text, reply_markup=get_info_markup)


@dp.message_handler(text='ℹ️Получить инфо')
async def get_info(message: Message, state: FSMContext):
    user_id, username = message.from_user.id, message.from_user.username
    logger.debug(f"ID: {user_id} ; Username: @{username} ; Text: Нажал на \"Получить инфо\"")
    await state.set_state('wait_geo')
    await message.answer('Пришли геолокацию по которой будет идти поиск', reply_markup=cancel_markup)


@dp.message_handler(text='📛Отмена', state='*')
async def cancel(message: Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Отменено!', reply_markup=get_info_markup)


@dp.message_handler(content_types=['location'], state='wait_geo')
async def get_location(message: Message, state: FSMContext):
    user_id, username = message.from_user.id, message.from_user.username
    latitude, longitude = message.location.latitude, message.location.longitude
    logger.debug(
        f"ID: {user_id} ; Username: @{username} ; Text: Прислал координаты: {latitude}  {longitude}")

    addr_object = get_addr(latitude, longitude)
    if addr_object:
        addr = addr_object[0]['value']
        await state.update_data(latitude=latitude, longitude=longitude, addr=addr)
        await state.set_state('wait_product')
        await message.answer('Введи название товара', reply_markup=cancel_markup)
    else:
        await state.reset_state()
        await message.answer('Произошла ошибка! Обратитесь к администратору', reply_markup=get_info_markup)


@dp.message_handler(state='wait_product')
async def get_product(message: Message, state: FSMContext):
    user_id, username = message.from_user.id, message.from_user.username
    logger.debug(
        f"ID: {user_id} ; Username: @{username} ; Text: Ввел название товара: {message.text}")

    await state.update_data(product=message.text)
    await state.set_state('wait_max_items')
    await message.answer('Введи максимальное количество товаров', reply_markup=cancel_markup)


@dp.message_handler(IsNumber(), state='wait_max_items')
async def get_max_items(message: Message, state: FSMContext):
    user_id, username = message.from_user.id, message.from_user.username
    logger.debug(
        f"ID: {user_id} ; Username: @{username} ; Text: Ввел макс. число товаров: {message.text}")

    await state.update_data(max_items=int(message.text))
