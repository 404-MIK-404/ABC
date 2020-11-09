from Models.Lecturer import Lecturer
from Models.Interval import Interval

class DatabaseManager:
    def __init__(self, db):
        self.db = db

    def add_lecturer(self, **kwargs):
        lecturer = Lecturer(first_name=kwargs["first_name"],
                            last_name=kwargs["last_name"],
                            patronymic=kwargs["patronymic"]
                            )
        self.db.session.add(lecturer)
        self.db.session.commit()

    def add_interval(self,**kwargs):
        interval = Interval(begintime=kwargs["begintime"],
                            endtime=kwargs["endtime"]
                            )
        self.db.session.add(interval)
        self.db.session.commit()