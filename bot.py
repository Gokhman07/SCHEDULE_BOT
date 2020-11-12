
import logging

from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import updater

from settings import TG_TOKEN
from handlers import *

#rom utility import get_keyboard


import os
PORT = int(os.environ.get('PORT', 5000))
updater=Updater(TG_TOKEN,use_context=True)
updater.start_webhook(listen="0.0.0.0",
port=int(PORT),
url_path=TG_TOKEN)
updater.bot.setWebhook('https://onatschedule.herokuapp.com/' + TG_TOKEN)


logging.basicConfig(format='%(asctime)s-$(levelname)s-$(message)s',
                    level=logging.INFO,
                    filename='bot.log')



def main():

    # описываем функцию (тело функции)
    # создадим переменную my_bot, с помощью которой будем взаимодействовать с нашим ботом
    my_bot = Updater(TG_TOKEN, use_context=True)
    logging.info('Start bot')
   
    
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))  # обработчик команды start

  
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, get_teach))  # обработчик текстового сообщения
    my_bot.start_polling()  # проверяет о наличии сообщений с платформы Telegram
    my_bot.idle()  # бот будет работать пока его не остановят


if __name__ == "__main__":
    main()
