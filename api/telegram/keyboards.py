from telegram import InlineKeyboardMarkup
from api.telegram.buttons import Buttons


class Keyboards():

  def __init__(self):
    self.button = Buttons()

  def main(self):
    keyboard = [
          [
            self.button.make_bet(),
            self.button.balance()
          ],
          [
            self.button.faq(),
            self.button.support()
          ]
        ]
    return InlineKeyboardMarkup(keyboard)

  def help(self):
    keyboard = [
          [
            self.button.support(),
            self.button.faq()
          ],
          [
            self.button.main()
          ]
        ]
    return InlineKeyboardMarkup(keyboard)

  def make_bet(self):
    keyboard = [
          [
            self.button.xbet(),
            self.button.line()
          ],
          [
            self.button.main()
          ]
        ]
    return InlineKeyboardMarkup(keyboard)

  def balance(self):
    keyboard = [
          [
            self.button.cashin(),
            self.button.cashout()
          ],
          [
            self.button.main()
          ]
        ]
    return InlineKeyboardMarkup(keyboard)


###############################################################################
