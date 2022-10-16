from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import parse

books_kb = InlineKeyboardMarkup()
for i in parse.main():
    books_kb.add(InlineKeyboardButton(text=i[0], callback_data='book_' + i[1]))

