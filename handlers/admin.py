from bot import dp
from aiogram import types
import os
import database
import json


async def get_info(message: types.Message):
    if message.chat.type == 'private' and json.loads(os.environ.get("ADMINS_ID")).count(message.chat.id):
        await message.answer(f"Количетво вызово: {database.read()['info']['all_requests_count']}")


def register_admin_handlers():
    dp.register_message_handler(get_info, commands=['info'])
