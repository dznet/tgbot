from api.telegram.messages import Messages
from api.telegram.keyboards import Keyboards


class Menu():

  def __init__(self):
    self.message = Messages()
    self.keyboard = Keyboards()

  def main(self, bot, update):
    update.message.reply_text(
                      self.message.run(),
                      parse_mode='Markdown',
                      reply_markup=self.keyboard.main()
                    )

  def stoped(self, bot, update):
    update.message.reply_text(
                      self.message.stoped(),
                      parse_mode='Markdown'
                    )

  def help(self, bot, update):
    update.message.reply_text(
                      self.message.help(),
                      parse_mode='Markdown',
                      reply_markup=self.keyboard.help()
                    )
