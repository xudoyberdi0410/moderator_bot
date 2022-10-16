# Create bot
import os
from aiogram import Bot, Dispatcher
from aiogram.bot.api import TelegramAPIServer


# local_server = TelegramAPIServer.from_base('http://localhost:8081')
bot = Bot(os.environ.get("BOT_TOKEN"))  # , server=local_server)
dp = Dispatcher(bot=bot)
