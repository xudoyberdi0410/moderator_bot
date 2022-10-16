# Moderator Bot
from handlers import client, admin
import logging
from aiogram import executor
from bot import bot, dp

logging.basicConfig(level=logging.INFO)

client.register_client_handlers()
admin.register_admin_handlers()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
