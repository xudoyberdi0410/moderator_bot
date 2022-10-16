import os
from aiogram import types
from keyboards import keyboard
import database
from bot import dp
import requests


async def start(message: types.Message):
    await message.answer("Привет👋.\nЯ бот помонщик🤖.\nПока что я умею только эти вещи:\n- отправлять учебники. Для этого отправьте команду /books.\nЕсли есть идеи предлагайте.")


async def books(message: types.Message):
    await message.answer('Выбирете учебник:', reply_markup=keyboard.books_kb)


async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.answer('Секундочку...')
    await callback_query.message.edit_reply_markup(reply_markup=None)
    await callback_query.message.edit_text('Подождите пожалуйста')
    getted_file = callback_query.data.split('_')[1]
    try:
        id = database.read()['books'][getted_file]
        await callback_query.message.answer_document(id)

    except Exception as e:
        print(f'[ERROR] {e}')

        file = requests.get(
            f"https://drive.google.com/u/0/uc?id={getted_file}&export=download")
        file_name = file.headers['Content-Disposition'].split(';')[1].split('=')[
            1].split('"')[1]
        with open(file_name, 'wb') as f:
            f.write(file.content)
        sended_file = await callback_query.message.answer_document(open(file_name, 'rb'))
        database.write('database.json', getted_file,
                       sended_file.document.file_id)
        os.remove(file_name)
    finally:
        database.write('database.json', 'all_requests_count', database.read()[
                       'info']['all_requests_count']+1, 'info')


def register_client_handlers():
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(books, commands=['books'])
    dp.register_callback_query_handler(
        process_callback_button1, lambda c: c.data.split('_')[0] == 'book')
