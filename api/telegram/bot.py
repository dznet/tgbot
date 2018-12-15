from sys import exc_info as error
from sys import stdout
from time import sleep
from api.telegram.menu import Menu
#DOC--->https://python-telegram-bot.readthedocs.io/
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import ConversationHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext import RegexHandler
from telegram.ext import Filters
from telegram.ext import Updater


class TelegramBot():

  __instances = {}

  def __init__(self, token):
    self.menu = Menu()
    self.updater = Updater(token)
    self.__instances[token] = self
    self.bot = self.updater.bot.get_me()
    self.dp = self.updater.dispatcher

    self.dp.add_handler(
                CommandHandler('start',
                               self.menu.main,
                               pass_user_data=True
                               )
              )
    self.dp.add_handler(
                CommandHandler('stop',
                               self.menu.stoped,
                               pass_user_data=True
                               )
              )
    self.dp.add_handler(
                CommandHandler('help',
                               self.menu.help,
                               pass_user_data=True
                               )
              )
    self.dp.add_handler(
                MessageHandler(Filters.text,
                               self.menu.main,
                               pass_user_data=True
                               )
              )

  @classmethod
  def get_instance(class_, token):
    return class_.__instances[token]

  def start(self):
    self.updater.start_polling()

  def stop(self):
    self.updater.stop()
