from sys import exc_info as error
from time import sleep
#DOC--->https://docs.pyrogram.ml/
from pyrogram import Client
from pyrogram import MessageHandler
from pyrogram.api.errors import Flood


class TelegramClient():

  __instances = {}

  def __init__(self, api_id, api_hash):
    self.client = Client(__name__, api_id, api_hash)
    self.__instances[api_hash] = self
    self.client.add_handler(MessageHandler(self.read_updates))

  def start(self):
    self.client.start()

  def stop(self):
    self.client.stop()

  def read_updates(self, client, message):
    print(message, '\n\n>>>\n\n', client)
