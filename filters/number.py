from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from keyboards import cancel_markup


class IsNumber(BoundFilter):
    async def check(self, message: Message) -> bool:
        if message.text.isdigit():
            return True

        await message.answer('Вы должны ввести число! Повторите попытку', reply_markup=cancel_markup)
