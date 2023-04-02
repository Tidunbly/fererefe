import logging
import datetime
from aiogram import Bot, types, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Dispatcher
from aiogram.dispatcher.webhook import SendMessage


# Enable logging
log_time = datetime.datetime.now().strftime('%d-%m-%Y')
logging.basicConfig(level=logging.INFO, filename=f'{log_time}-log.log')


# Bot Token
API_TOKEN = '6210082109:AAE3zRsenHa4JIlfJ_4vNLAC6V1aMpGlYi8'


# Bot settings
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


# Commands
@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    return SendMessage(message.chat.id, message.text)


@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
    return SendMessage(message.chat.id, 'You just typed /help.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)