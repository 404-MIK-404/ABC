from Managers.DatabaseManager import DatabaseManager
from extensions import db
from app import app


def CreateLecturer():
    db_manager = DatabaseManager(db)
    db_manager.add_lecturer(first_name='Гудкова', last_name='Ирина', patronymic='Алексеевна')
    db_manager.add_lecturer(first_name='Волков', last_name='Андрей', patronymic='Иванович')
    db_manager.add_lecturer(first_name='Гуриков', last_name='Сергей', patronymic='Ростиславович')
    db_manager.add_lecturer(first_name='Воробейчиков', last_name='Леонид', patronymic='Александрович')
    db_manager.add_lecturer(first_name='Мальцева', last_name='Светлана', patronymic='Николаевна')

def CreateIntervalTime():
    db_manager = DatabaseManager(db)
    db_manager.add_interval(begintime='9:30',endtime='11:05')

with app.app_context():
    db.create_all()
    CreateLecturer()
    CreateIntervalTime()






