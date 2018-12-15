from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from api.basemodels import db
from run import api

migrate = Migrate(api, db)
manager = Manager(api)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()
