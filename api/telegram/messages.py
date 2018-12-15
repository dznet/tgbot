from api.basemodels import datetime


class Messages():

  def __init__(self):
    pass

  def run(self):
    return '*EasyBetBot* successfuly runing @ {}'.format(datetime.now())

  def shutdown(self):
    return '*EasyBetBot* goes shutdown @ {}...'.format(datetime.now())

  def crash(self):
    return 'Oops! *EasyBetBot* error @ {}'.format(datetime.now())

  def help(self):
    return 'Hey! What time is it? Help coming soon!'
