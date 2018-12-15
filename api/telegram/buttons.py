from telegram import InlineKeyboardButton
from telegram import KeyboardButton


class Buttons():

  def __init__(self):
    pass

  def make_bet(self):
    return InlineKeyboardButton(u'\U0001F680 Сделать ставку',
                                callback_data='bet'
                                )

  def balance(self):
    return InlineKeyboardButton(u'\U0001F4B5 Баланс',
                                callback_data='balance'
                                )

  def support(self):
    return InlineKeyboardButton(u'\U0001F4BC Поддержка',
                                callback_data='support'
                                )

  def faq(self):
    return InlineKeyboardButton(u'\U0001F4E5 FAQ',
                                callback_data='faq'
                                )

  def xbet(self):
    return InlineKeyboardButton(u'\U0001F303 1xbet',
                                callback_data='xbet'
                                )

  def line(self):
    return InlineKeyboardButton(u'\U0001F303 Линия',
                                callback_data='line'
                                )

  def main(self):
    return InlineKeyboardButton(u'\U0001F303 Назад',
                                callback_data='main'
                                )

  def cashin(self):
    return InlineKeyboardButton(u'\U0001F303 Пополнить',
                                callback_data='cashin'
                                )

  def cashout(self):
    return InlineKeyboardButton(u'\U0001F303 Вывести',
                                callback_data='cashout'
                                )

###############################################################################
