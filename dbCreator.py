from Managers.DatabaseManager import DatabaseManager
from extensions import db
from app import app


def CreateIntervalTime():
    db_manager = DatabaseManager(db)
    db_manager.add_interval(begintime='9:30 - 11:05')
    db_manager.add_interval(begintime='11:20 - 12:55')
    db_manager.add_interval(begintime='13:10 - 14:45')
    db_manager.add_interval(begintime='15:25 - 17:00')
    db_manager.add_interval(begintime='17:15 - 18:50')


with app.app_context():
    db.create_all()
    CreateIntervalTime()






