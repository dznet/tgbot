from apscheduler.schedulers.background import BackgroundScheduler

class Scheduler(BackgroundScheduler):

  def __init__(self):
    super().__init__()

  def schedule_event(self, event, time, chat_id):
    self.add_job(event, run_date=time, args=chat_id)
